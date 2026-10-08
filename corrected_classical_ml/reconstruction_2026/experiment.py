"""2026 post-MSc exploratory baselines; NOT the original 2024 thesis code."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
from sklearn.model_selection import StratifiedGroupKFold, StratifiedKFold
from sklearn.preprocessing import StandardScaler

CLASSES = ("B", "C", "M", "X")
FEATURES = (
    "TOTUSJH", "TOTBSQ", "TOTPOT", "TOTUSJZ", "ABSNJZH",
    "SAVNCPP", "USFLUX", "AREA_ACR", "TOTFZ", "MEANPOT",
    "R_VALUE", "EPSZ", "SHRGT45",
)
EXPECTED_COUNTS = {"B": 128, "C": 552, "M": 142, "X": 23}


def load_data(path: Path, *, verify_upstream: bool = True) -> pd.DataFrame:
    data = pd.read_csv(path)
    needed = ["Flare Class", "Flare Date", "AR", *FEATURES]
    missing = sorted(set(needed) - set(data.columns))
    if missing:
        raise ValueError(f"Required upstream columns absent: {missing}")
    data = data.copy()
    data["target"] = data["Flare Class"].astype(str).str.strip().str.upper().str[0]
    if not data["target"].isin(CLASSES).all():
        raise ValueError("Unrecognised flare class in upstream CSV")
    data["timestamp"] = pd.to_datetime(data["Flare Date"], format="%m/%d/%Y %H:%M", errors="raise")
    data["AR"] = data["AR"].astype(str)
    for feature in FEATURES:
        data[feature] = pd.to_numeric(data[feature], errors="raise")
    if not np.isfinite(data[list(FEATURES)].to_numpy(dtype=float)).all():
        raise ValueError("Non-finite SHARP parameter values detected")
    if verify_upstream:
        counts = data["target"].value_counts().to_dict()
        if len(data) != 845 or counts != EXPECTED_COUNTS or data["AR"].nunique() != 472:
            raise ValueError("Input does not match the thesis-reported reference dataset counts")
    return data


def tss_ovr(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float | None]:
    """One-vs-rest TSS per class: recall minus false-positive rate."""
    matrix = confusion_matrix(y_true, y_pred, labels=CLASSES)
    total = matrix.sum()
    values: dict[str, float | None] = {}
    for i, cls in enumerate(CLASSES):
        tp = matrix[i, i]
        fn = matrix[i, :].sum() - tp
        fp = matrix[:, i].sum() - tp
        tn = total - tp - fn - fp
        values[cls] = float(tp / (tp + fn) - fp / (fp + tn)) if (tp + fn) and (fp + tn) else None
    return values


def build_pipeline(model_name: str, sampling: str, seed: int) -> Pipeline:
    classifiers = {
        "extra_trees": ExtraTreesClassifier(n_estimators=150, random_state=seed, n_jobs=1),
        "random_forest": RandomForestClassifier(n_estimators=150, random_state=seed, n_jobs=1),
    }
    if model_name not in classifiers:
        raise ValueError(f"Unsupported model: {model_name}")
    steps: list[tuple[str, object]] = [("scale", StandardScaler())]
    if sampling == "under":
        steps.append(("sampler", RandomUnderSampler(random_state=seed)))
    elif sampling == "smote":
        steps.append(("sampler", SMOTE(random_state=seed, k_neighbors=3)))
    elif sampling != "none":
        raise ValueError(f"Unsupported sampler: {sampling}")
    steps.append(("model", classifiers[model_name]))
    return Pipeline(steps)


def evaluate(data: pd.DataFrame, *, mode: str = "stratified", model: str = "extra_trees",
             sampling: str = "none", seed: int = 42, folds: int = 5) -> dict:
    if folds < 2:
        raise ValueError("folds must be >= 2")
    x = data.loc[:, FEATURES].to_numpy(dtype=float)
    y = data["target"].to_numpy()
    groups = data["AR"].to_numpy()
    if mode == "stratified":
        splitter = StratifiedKFold(n_splits=folds, shuffle=True, random_state=seed)
        splits = splitter.split(x, y)
    elif mode == "grouped":
        splitter = StratifiedGroupKFold(n_splits=folds, shuffle=True, random_state=seed)
        splits = splitter.split(x, y, groups=groups)
    elif mode == "chronological":
        order = np.argsort(data["timestamp"].to_numpy())
        cutoff = int(len(order) * 0.8)
        if not 0 < cutoff < len(order):
            raise ValueError("Too few rows for chronological holdout")
        splits = [(order[:cutoff], order[cutoff:])]
    else:
        raise ValueError(f"Unsupported evaluation mode: {mode}")

    results = []
    for fold_number, (train, test) in enumerate(splits, start=1):
        if len(set(y[train])) != len(CLASSES):
            raise ValueError(f"Training fold {fold_number} lacks a flare class")
        missing_test_classes = [c for c in CLASSES if c not in set(y[test])]
        estimator = build_pipeline(model, sampling, seed + fold_number)
        estimator.fit(x[train], y[train])
        predictions = estimator.predict(x[test])
        scores = tss_ovr(y[test], predictions)
        matrix = confusion_matrix(y[test], predictions, labels=CLASSES)
        class_diagnostics = {}
        for i, cls in enumerate(CLASSES):
            tp = int(matrix[i, i])
            fn = int(matrix[i, :].sum() - tp)
            fp = int(matrix[:, i].sum() - tp)
            tn = int(matrix.sum() - tp - fn - fp)
            recall = float(tp / (tp + fn)) if tp + fn else None
            specificity = float(tn / (tn + fp)) if tn + fp else None
            class_diagnostics[cls] = {
                "support": tp + fn, "predicted": tp + fp,
                "tp": tp, "fn": fn, "fp": fp, "tn": tn,
                "recall": recall, "specificity": specificity,
                "precision": float(tp / (tp + fp)) if tp + fp else None,
                "one_vs_rest_bacc": (recall + specificity) / 2
                    if recall is not None and specificity is not None else None,
                "one_vs_rest_tss": recall + specificity - 1
                    if recall is not None and specificity is not None else None,
            }
        for cls in CLASSES:
            a, b = class_diagnostics[cls]["one_vs_rest_tss"], scores[cls]
            if a is None or b is None:
                if a is not None or b is not None:
                    raise AssertionError("TSS definition mismatch on missing class")
            elif not np.isclose(a, b, atol=1e-12):
                raise AssertionError("Disagreement in TSS calculation")
        shared_regions = len(set(groups[train]) & set(groups[test]))
        if mode == "grouped" and shared_regions:
            raise AssertionError("Grouped validation leaked an active-region identifier")
        if mode == "chronological" and data.iloc[train].timestamp.max() > data.iloc[test].timestamp.min():
            raise AssertionError("Chronological holdout was not temporally ordered")
        # Thesis equations 2-3: class-wise BACC=(TPR+TNR)/2 and TSS=TPR-FPR.
        # They are averaged over four one-versus-rest classes. If a held-out
        # test fold lacks any class, a four-class aggregate is undefined.
        all_four = all(v is not None for v in scores.values())
        thesis_style_tss = float(np.mean(list(scores.values()))) if all_four else None
        thesis_style_bacc = (1.0 + thesis_style_tss) / 2.0 if all_four else None
        results.append({
            "fold": fold_number,
            "train_size": int(len(train)), "test_size": int(len(test)),
            "train_classes": {k: int(sum(y[train] == k)) for k in CLASSES},
            "test_classes": {k: int(sum(y[test] == k)) for k in CLASSES},
            "shared_active_regions": shared_regions,
            "confusion_matrix_labels": list(CLASSES),
            "confusion_matrix": matrix.tolist(),
            "per_class_diagnostics": class_diagnostics,
            "four_class_evaluable": not missing_test_classes,
            "unrepresented_test_classes": missing_test_classes,
            "balanced_accuracy": float(balanced_accuracy_score(y[test], predictions)),
            "sklearn_macro_recall": float(balanced_accuracy_score(y[test], predictions)),
            "thesis_style_ovr_bacc": thesis_style_bacc,
            "thesis_style_ovr_tss": thesis_style_tss,
            "tss_ovr_by_class": scores,
            "tss_ovr_macro": float(np.mean([v for v in scores.values() if v is not None]))
            if any(v is not None for v in scores.values()) else None,
        })
    return {
        "analysis": "NEW POST-MSC 2026 RECONSTRUCTION; NOT THE 2024 THESIS EXPERIMENTS",
        "data_rows": int(len(data)), "source_classes": data["target"].value_counts().to_dict(),
        "mode": mode, "model": model, "sampling": sampling, "seed": seed,
        "folds": results,
        "mean_balanced_accuracy": float(np.mean([v["balanced_accuracy"] for v in results])),
        "mean_thesis_style_ovr_bacc": float(np.mean([v["thesis_style_ovr_bacc"] for v in results]))
            if all(v["thesis_style_ovr_bacc"] is not None for v in results) else None,
        "mean_thesis_style_ovr_tss": float(np.mean([v["thesis_style_ovr_tss"] for v in results]))
            if all(v["thesis_style_ovr_tss"] is not None for v in results) else None,
        "all_splits_four_class_evaluable": all(v["four_class_evaluable"] for v in results),
        "evaluation_warning": ("At least one test split lacks a flare class; reported averages "
                              "do not estimate full four-class performance."
                              if not all(v["four_class_evaluable"] for v in results) else None),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path(__file__).parent / "local_data" / "flaringar_original_data.csv")
    parser.add_argument("--mode", choices=("stratified", "grouped", "chronological"), default="stratified")
    parser.add_argument("--model", choices=("extra_trees", "random_forest"), default="extra_trees")
    parser.add_argument("--sampling", choices=("none", "under", "smote"), default="none")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = evaluate(load_data(args.data), mode=args.mode, model=args.model,
                      sampling=args.sampling, seed=args.seed, folds=args.folds)
    payload = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
        print(f"New reconstruction results saved: {args.output}")
    else:
        print(payload)


if __name__ == "__main__":
    main()
