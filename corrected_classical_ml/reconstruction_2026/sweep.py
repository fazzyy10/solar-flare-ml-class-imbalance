"""Execute a predeclared 18-cell methodological audit on the public DeepSun dataset.

This is new exploratory post-MSc work, not reproduction of the 2024 notebook.
The resulting fold averages are descriptive, not an independent holdout estimate.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
import imblearn
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold

from experiment import CLASSES, FEATURES, evaluate, load_data
from fetch_upstream import GIT_BLOB_SHA1, UPSTREAM_COMMIT, URL, verify_git_blob

BASE = Path(__file__).resolve().parent
DATA = BASE / "local_data" / "flaringar_original_data.csv"
OUT = BASE / "local_results"
MODELS = ("extra_trees", "random_forest")
SAMPLES = ("none", "under", "smote")
MODES = ("stratified", "grouped", "chronological")
SEED = 42
FOLDS = 5


def dataset_profile(data: pd.DataFrame, raw_bytes: bytes) -> dict:
    if not verify_git_blob(raw_bytes):
        raise RuntimeError("Public upstream input does not match the pinned Git blob")
    dates = data["timestamp"].dt.year
    groups_per_class = data.groupby("target")["AR"].nunique()
    group_classes = data.groupby("AR")["target"].nunique()
    s = data.groupby("AR").size()
    return {
        "source_url": URL, "source_commit": UPSTREAM_COMMIT, "git_blob_sha1": GIT_BLOB_SHA1,
        "dataset_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "dataset_rows": int(len(data)), "feature_count": len(FEATURES),
        "classes": data.target.value_counts().sort_index().to_dict(),
        "active_regions": int(data.AR.nunique()),
        "repeated_active_regions": int((s > 1).sum()),
        "maximum_observations_in_one_region": int(s.max()),
        "active_regions_with_multiple_target_classes": int((group_classes > 1).sum()),
        "unique_regions_by_class": groups_per_class.to_dict(),
        "events_by_year_class": pd.crosstab(dates, data.target).to_dict(orient="index"),
        "zero_missing_predictor_cells": bool(data[list(FEATURES)].notna().all().all()),
        "unique_exact_rows": int(data[["Flare Class", "Flare Date", "AR", *FEATURES]].drop_duplicates().shape[0]),
        "range_checks": {str(c): [float(data[c].min()), float(data[c].max())] for c in FEATURES},
        "versions": {"python": sys.version.split()[0], "pandas": pd.__version__,
                     "numpy": np.__version__, "scikit-learn": sklearn.__version__,
                     "imbalanced-learn": imblearn.__version__},
    }


def split_diagnostics(data: pd.DataFrame) -> dict:
    x = data[list(FEATURES)].to_numpy()
    y = data.target.to_numpy()
    g = data.AR.to_numpy()
    diagnostics = {}
    for mode in MODES:
        if mode == "stratified":
            splits = list(StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=SEED).split(x, y))
        elif mode == "grouped":
            splits = list(StratifiedGroupKFold(n_splits=FOLDS, shuffle=True, random_state=SEED).split(x, y, groups=g))
        else:
            order = np.argsort(data["timestamp"].to_numpy())
            cutoff = int(len(order) * 0.8)
            splits = [(order[:cutoff], order[cutoff:])]
        arr = []
        for i, (train, test) in enumerate(splits, 1):
            ar_overlap = len(set(g[train]) & set(g[test]))
            start_end = [str(data.iloc[train].timestamp.min()), str(data.iloc[train].timestamp.max()),
                         str(data.iloc[test].timestamp.min()), str(data.iloc[test].timestamp.max())]
            rec = {"fold": i, "train_n": int(len(train)), "test_n": int(len(test)),
                   "shared_active_regions": ar_overlap,
                   "train_class_counts": {c: int(sum(y[train] == c)) for c in CLASSES},
                   "test_class_counts": {c: int(sum(y[test] == c)) for c in CLASSES},
                   "date_ranges": start_end}
            if mode == "grouped" and ar_overlap:
                raise AssertionError("Grouped CV leaks active-region IDs")
            if mode == "chronological" and not data.iloc[train].timestamp.max() <= data.iloc[test].timestamp.min():
                raise AssertionError("Chronological test contains past training date")
            arr.append(rec)
        diagnostics[mode] = arr
    return diagnostics


def main() -> None:
    OUT.mkdir(exist_ok=True, parents=True)
    raw = DATA.read_bytes()
    df = load_data(DATA)
    profile = dataset_profile(df, raw)
    diagnostics = split_diagnostics(df)
    (OUT / "data_profile.json").write_text(json.dumps(profile, indent=2), encoding="utf-8")
    (OUT / "split_diagnostics.json").write_text(json.dumps(diagnostics, indent=2), encoding="utf-8")
    print("DATA PROFILE: " + json.dumps({k: profile[k] for k in
          ("dataset_sha256","dataset_rows","classes","active_regions","repeated_active_regions",
           "active_regions_with_multiple_target_classes","unique_regions_by_class")} ),flush=True)
    print("SPLIT LEAKAGE: " + json.dumps(
          {k: [x["shared_active_regions"] for x in a] for k, a in diagnostics.items()}),flush=True)
    records, folds, errors = [], [], []
    for mode, model, sampling in itertools.product(MODES, MODELS, SAMPLES):
        key = f"{mode}_{model}_{sampling}"
        print("RUN " + key, flush=True)
        now = time.perf_counter()
        try:
            result = evaluate(df, mode=mode, model=model, sampling=sampling,
                              seed=SEED, folds=FOLDS)
            elapsed = round(time.perf_counter() - now, 3)
            (OUT / (key + ".json")).write_text(json.dumps(result, indent=2), encoding="utf-8")
            scores = [f["tss_ovr_macro"] for f in result["folds"] if f["tss_ovr_macro"] is not None]
            blank = sum(any(v == 0 for v in f["test_classes"].values()) for f in result["folds"])
            entry = {
                "mode": mode, "model": model, "sampling": sampling,
                "test_folds": len(result["folds"]), "missing_class_folds": blank,
                "mean_bacc_reported": result["mean_balanced_accuracy"],
                "sd_bacc_between_folds": float(np.std([f["balanced_accuracy"] for f in result["folds"]], ddof=1))
                 if len(result["folds"]) > 1 else None,
                "mean_macro_ovr_tss": float(np.mean(scores)) if scores else None,
                "elapsed_seconds": elapsed,
                "status": "ok",
            }
            records.append(entry)
            for f in result["folds"]:
                folds.append({"mode": mode, "model": model, "sampling": sampling,
                              "fold": f["fold"], "balanced_accuracy": f["balanced_accuracy"],
                              "macro_ovr_tss": f["tss_ovr_macro"], "train_size": f["train_size"],
                              "test_size": f["test_size"], **{"test_"+str(k):v for k,v in f["test_classes"].items()},
                              **{"tss_"+str(k):v for k,v in f["tss_ovr_by_class"].items()}})
            print("RESULT " + key + ": " + json.dumps(entry),flush=True)
        except Exception as error:
            entry={"mode":mode, "model":model,"sampling":sampling,
                   "status":"error","error":type(error).__name__+": "+str(error)}
            errors.append(entry)
            records.append(entry)
            print("ERROR " + key + ": " + str(error),flush=True)
    pd.DataFrame(records).to_csv(OUT / "matrix_summary.csv",index=False)
    pd.DataFrame(folds).to_csv(OUT / "fold_metrics.csv",index=False)
    (OUT / "failed_cases.json").write_text(json.dumps(errors, indent=2),encoding="utf-8")
    (OUT / "run_metadata.json").write_text(json.dumps(
        {"historical_2024_reported_extra_trees_BACC":0.829979,
         "historical_2024_reported_extra_trees_TSS":0.659958,
         "historical_comparability":"not established: different preprocessing, different CV, sample design, models, TSS aggregation",
         "seed": SEED, "folds_for_CV": FOLDS,
         "models": MODELS, "sampling": SAMPLES, "modes": MODES,
         "runs_successful": len(records)-len(errors), "runs_failed": len(errors),
         "warning":"missing_class_folds means standard sklearn balanced_accuracy_score averages only classes present in test; these results cannot be called full four-class BACC."},
         indent=2),encoding="utf-8")
    print("FINAL SUMMARY " + json.dumps({"runs":len(records),"successful":len(records)-len(errors),"errors":errors}),flush=True)
    if errors:
        raise SystemExit("At least one configuration failed, see local_results/failed_cases.json")


if __name__ == "__main__":
    main()
