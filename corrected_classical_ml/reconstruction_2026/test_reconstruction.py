from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from experiment import CLASSES, FEATURES, build_pipeline, evaluate, load_data, tss_ovr
from fetch_upstream import GIT_BLOB_SHA1, verify_git_blob


def synthetic_data() -> pd.DataFrame:
    rng = np.random.default_rng(123)
    n = 120
    return pd.DataFrame({
        **{col: rng.normal(loc=i, size=n) for i, col in enumerate(FEATURES)},
        "target": list(CLASSES) * 30,
        "AR": [str(i // 4) for i in range(n)],
        "timestamp": pd.date_range("2020-01-01", periods=n, freq="D"),
    })


def test_blob_verification_rejects_unrelated_data():
    assert len(GIT_BLOB_SHA1) == 40
    assert not verify_git_blob(b"not the original GitHub CSV")


def test_load_data_and_schema(tmp_path: Path):
    d = synthetic_data()
    raw = d.loc[:, FEATURES].copy()
    raw.insert(0, "AR", d["AR"])
    raw.insert(0, "Flare Date", d["timestamp"].dt.strftime("%m/%d/%Y %H:%M"))
    raw.insert(0, "Flare Class", d["target"] + "12")
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)
    loaded = load_data(path, verify_upstream=False)
    assert len(loaded) == 120
    assert set(loaded.target) == set(CLASSES)
    with pytest.raises(ValueError, match="reference dataset"):
        load_data(path, verify_upstream=True)


def test_score_exact_prediction():
    y = np.array(list(CLASSES) * 3)
    per_class = tss_ovr(y, y)
    assert all(x == 1.0 for x in per_class.values())


@pytest.mark.parametrize("sampling", ["none", "under", "smote"])
def test_fold_safe_train_and_evaluate(sampling: str):
    df = synthetic_data()
    output = evaluate(df, sampling=sampling, folds=3)
    assert output["analysis"].startswith("NEW POST-MSC")
    assert len(output["folds"]) == 3
    assert all(0 <= z["balanced_accuracy"] <= 1 for z in output["folds"])
    estimator = build_pipeline("extra_trees", sampling, 10)
    if sampling != "none":
        assert "sampler" in estimator.named_steps


def test_chronological_holdout():
    result = evaluate(synthetic_data(), mode="chronological")
    assert len(result["folds"]) == 1
    assert result["folds"][0]["train_size"] == 96
    assert result["folds"][0]["test_size"] == 24


def test_ovr_metric_identity():
    labels = np.array(["B","C","M","X"] * 6)
    predicted = labels.copy()
    predicted[0] = "C"
    scores = tss_ovr(labels, predicted)
    assert all(v is not None for v in scores.values())
    tss = np.mean(list(scores.values()))
    assert 0.0 <= (1.0 + tss) / 2.0 <= 1.0

def test_missing_class_is_flagged_not_extrapolated():
    df = synthetic_data()
    # Force the last chronological observations to lack X.
    final = df["timestamp"] >= df["timestamp"].nlargest(24).min()
    df.loc[final, "target"] = "C"
    result = evaluate(df, mode="chronological")
    assert result["all_splits_four_class_evaluable"] is False
    assert "X" in result["folds"][0]["unrepresented_test_classes"]
    assert result["mean_thesis_style_ovr_bacc"] is None

def test_grouped_splits_have_no_active_region_overlap():
    from sklearn.model_selection import StratifiedGroupKFold
    df = synthetic_data()
    x = df.loc[:, FEATURES].to_numpy(dtype=float)
    y = df.target.to_numpy()
    groups = df.AR.to_numpy()
    for tr, te in StratifiedGroupKFold(n_splits=3, shuffle=True, random_state=7).split(x, y, groups):
        assert set(groups[tr]).isdisjoint(set(groups[te]))

def test_nonfinite_feature_rejected(tmp_path: Path):
    df = synthetic_data()
    raw = df.loc[:, FEATURES].copy()
    raw.insert(0, "AR", df.AR)
    raw.insert(0, "Flare Date", df.timestamp.dt.strftime("%m/%d/%Y %H:%M"))
    raw.insert(0, "Flare Class", df.target + "12")
    raw.loc[0, FEATURES[0]] = float("inf")
    file = tmp_path / "infinite.csv"
    raw.to_csv(file, index=False)
    with pytest.raises(ValueError, match="Non-finite"):
        load_data(file, verify_upstream=False)


def test_fold_result_retains_class_support_confusion_and_region_overlap():
    df = synthetic_data()
    result = evaluate(df, mode="grouped", folds=3)
    for fold in result["folds"]:
        assert fold["shared_active_regions"] == 0
        matrix = np.asarray(fold["confusion_matrix"])
        assert matrix.shape == (4, 4)
        assert int(matrix.sum()) == fold["test_size"]
        assert sum(item["support"] for item in fold["per_class_diagnostics"].values()) == fold["test_size"]
        for cls in CLASSES:
            diagnostic = fold["per_class_diagnostics"][cls]
            if diagnostic["one_vs_rest_tss"] is not None:
                assert diagnostic["one_vs_rest_tss"] == pytest.approx(fold["tss_ovr_by_class"][cls])


def test_missing_class_must_be_explicit():
    df = synthetic_data()
    cutoff = df["timestamp"].nlargest(24).min()
    df.loc[df["timestamp"] >= cutoff, "target"] = "C"
    result = evaluate(df, mode="chronological")
    assert not result["all_splits_four_class_evaluable"]
    assert "X" in result["folds"][0]["unrepresented_test_classes"]
    assert result["folds"][0]["per_class_diagnostics"]["X"]["support"] == 0
    assert result["folds"][0]["per_class_diagnostics"]["X"]["one_vs_rest_tss"] is None
    assert result["mean_thesis_style_ovr_bacc"] is None



def test_historical_execution_count_is_explicitly_unverified():
    """Do not let a historical arithmetic inconsistency become a reproducibility claim."""
    root = Path(__file__).resolve().parents[2]
    methods=(root/"docs/METHODS_SUBMITTED.md").read_text(encoding="utf-8")
    for evidence in ("29,400", "28,140", "2,010", "201 × 10"):
        assert evidence in methods
    assert "unresolved arithmetic inconsistency" in methods


def test_public_homepage_does_not_claim_operational_forecasting():
    root = Path(__file__).resolve().parents[2]
    readme=(root/"README.md").read_text(encoding="utf-8")
    assert "quiet periods" in readme
    assert "lead time" in readme
    assert "does not demonstrate a working 24-hour operational forecasting service" in readme
