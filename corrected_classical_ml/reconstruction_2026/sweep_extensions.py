"""Additional pre-declared stability and leakage-free temporal evaluations.

These 2026 sensitivity analyses supplement, but do not reproduce, the MSc study.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score

from experiment import CLASSES, FEATURES, build_pipeline, evaluate, load_data, tss_ovr
from sweep import MODELS, SAMPLES, OUT, DATA

BASE = Path(__file__).resolve().parent
STABILITY_SEEDS = (73, 2024)
TIME_CUTOFF = pd.Timestamp("2014-01-01")


def full_ovr_score(truth: np.ndarray, predicted: np.ndarray) -> tuple[float | None, float | None]:
    """Four-class macro one-vs-rest TSS and BACC; undefined if held-out class absent."""
    per_class = tss_ovr(truth, predicted)
    if not all(value is not None for value in per_class.values()):
        return None, None
    mean_tss = float(np.mean(list(per_class.values())))
    return float((1.0 + mean_tss) / 2.0), mean_tss


def temporal_all_class_holdout(data: pd.DataFrame, model: str, sampling: str) -> dict:
    earlier = data.timestamp < TIME_CUTOFF
    later = ~earlier
    train = data.loc[earlier].copy()
    holdout = data.loc[later].copy()
    # Exactly one upstream active region straddles this date boundary. Retain
    # the training events; embargo all later events from already-seen regions.
    seen = set(train.AR)
    excluded = holdout.AR.isin(seen)
    excluded_n = int(excluded.sum())
    holdout = holdout.loc[~excluded].copy()
    assert not (set(train.AR) & set(holdout.AR))
    assert train.timestamp.max() < holdout.timestamp.min()
    assert set(train.target) == set(CLASSES) == set(holdout.target)
    pipeline = build_pipeline(model, sampling, 42)
    pipeline.fit(train.loc[:, FEATURES].to_numpy(dtype=float), train.target.to_numpy())
    pred = pipeline.predict(holdout.loc[:, FEATURES].to_numpy(dtype=float))
    bacc, tss = full_ovr_score(holdout.target.to_numpy(), pred)
    assert bacc is not None and tss is not None
    return {
        "type": "2014-start-chronological-holdout-embargoed",
        "train_cutoff_exclusive": str(TIME_CUTOFF),
        "train_size": int(len(train)),
        "test_size": int(len(holdout)),
        "excluded_test_events_due_to_region_overlap": excluded_n,
        "train_counts": train.target.value_counts().reindex(CLASSES,fill_value=0).to_dict(),
        "test_counts": holdout.target.value_counts().reindex(CLASSES,fill_value=0).to_dict(),
        "model":model, "sampling":sampling, "seed":42,
        "mean_thesis_style_ovr_bacc":bacc,
        "mean_thesis_style_ovr_tss":tss,
        "sklearn_macro_recall":float(balanced_accuracy_score(holdout.target.to_numpy(),pred)),
        "class_tss":tss_ovr(holdout.target.to_numpy(),pred),
        "caveat":"Cutoff selected for sensitivity analysis after inspecting time class availability; not an unseen independent final model-selection test.",
    }


def main() -> None:
    data = load_data(DATA)
    OUT.mkdir(parents=True,exist_ok=True)
    stability = []
    for mode in ("stratified","grouped"):
        for model in MODELS:
            for sampling in SAMPLES:
                for seed in STABILITY_SEEDS:
                    result=evaluate(data,mode=mode,model=model,sampling=sampling,seed=seed,folds=5)
                    stability.append({
                        "mode":mode,"model":model,"sampling":sampling,"seed":seed,
                        "mean_thesis_style_ovr_bacc":result["mean_thesis_style_ovr_bacc"],
                        "mean_thesis_style_ovr_tss":result["mean_thesis_style_ovr_tss"],
                        "four_class_evaluable":result["all_splits_four_class_evaluable"],
                        "fold_ovr_bacc":json.dumps([fold["thesis_style_ovr_bacc"] for fold in result["folds"]]),
                    })
                    print("STABILITY",mode,model,sampling,seed,"BACC",result["mean_thesis_style_ovr_bacc"],flush=True)
    temporal=[]
    for model in MODELS:
        for sampling in SAMPLES:
            r=temporal_all_class_holdout(data,model,sampling)
            temporal.append(r)
            print("TEMPORAL",model,sampling,"BACC",r["mean_thesis_style_ovr_bacc"],"TSS",r["mean_thesis_style_ovr_tss"],"excluded",r["excluded_test_events_due_to_region_overlap"],flush=True)
    pd.DataFrame(stability).to_csv(OUT/"seed_sensitivity_extra.csv",index=False)
    pd.DataFrame([{
        "model":r["model"],"sampling":r["sampling"],"train_size":r["train_size"],"test_size":r["test_size"],
        "embargoed_test_events":r["excluded_test_events_due_to_region_overlap"],
        "thesis_style_ovr_bacc":r["mean_thesis_style_ovr_bacc"],
        "thesis_style_ovr_tss":r["mean_thesis_style_ovr_tss"],
        "sklearn_macro_recall":r["sklearn_macro_recall"],**{"class_tss_"+k:v for k,v in r["class_tss"].items()}
    } for r in temporal]).to_csv(OUT/"2014_chronological_holdout.csv",index=False)
    (OUT/"2014_chronological_holdout.json").write_text(json.dumps(temporal,indent=2),encoding="utf-8")
    print("EXTRA PASS",len(stability),"repeat-seed evaluations and",len(temporal),"chronological evaluations",flush=True)


if __name__=="__main__":
    main()
