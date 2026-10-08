"""Fail CI on incomplete, mislabeled or implausible new 2026 results."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from experiment import CLASSES
from fetch_upstream import EXPECTED_SHA256

HERE = Path(__file__).resolve().parent
OUT = HERE / "local_results"
SOURCE = HERE / "local_data" / "flaringar_original_data.csv"

def main() -> None:
    raw = SOURCE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256, "Input SHA-256 mismatch"
    profile = json.loads((OUT / "data_profile.json").read_text())
    assert profile["dataset_sha256"] == EXPECTED_SHA256
    assert profile["dataset_rows"] == 845 and profile["active_regions"] == 472
    assert profile["classes"] == {"B":128,"C":552,"M":142,"X":23}
    assert profile["feature_count"] == 13
    splits = json.loads((OUT / "split_diagnostics.json").read_text())
    assert len(splits["stratified"]) == len(splits["grouped"]) == 5
    assert len(splits["chronological"]) == 1
    assert all(z["shared_active_regions"] == 0 for z in splits["grouped"])
    assert all(z["shared_active_regions"] > 0 for z in splits["stratified"])
    assert splits["chronological"][0]["test_class_counts"]["X"] == 0

    matrix = pd.read_csv(OUT / "matrix_summary.csv")
    assert len(matrix) == 18 and set(matrix.status) == {"ok"}
    assert set(matrix["mode"]) == {"stratified","grouped","chronological"}
    assert int(matrix["missing_class_folds"].sum()) == 6
    assert matrix.loc[matrix["mode"] == "chronological","mean_thesis_style_ovr_bacc"].isna().all()
    assert matrix.loc[matrix["mode"] != "chronological","mean_thesis_style_ovr_bacc"].between(0,1).all()
    repeat = pd.read_csv(OUT / "seed_sensitivity_extra.csv")
    assert len(repeat) == 24 and repeat["mean_thesis_style_ovr_bacc"].between(0,1).all()
    temporal = pd.read_csv(OUT / "2014_chronological_holdout.csv")
    assert len(temporal) == 6
    assert set(temporal.embargoed_test_events) == {1}
    assert set(temporal.train_size) == {481} and set(temporal.test_size) == {363}
    assert temporal["thesis_style_ovr_bacc"].between(0,1).all()
    assert temporal["thesis_style_ovr_tss"].between(-1,1).all()

    cases=0
    for p in sorted(OUT.glob("*.json")):
        if not p.stem.startswith(("stratified_", "grouped_", "chronological_")):
            continue
        if p.name in ("2014_chronological_holdout.json",):
            continue
        r=json.loads(p.read_text())
        assert r["analysis"].startswith("NEW POST-MSC")
        for fold in r["folds"]:
            c=np.asarray(fold["confusion_matrix"])
            assert c.shape == (4,4) and int(c.sum()) == fold["test_size"]
            assert sum(fold["test_classes"].values()) == fold["test_size"]
            assert sum(fold["train_classes"].values()) == fold["train_size"]
            assert all(fold["per_class_diagnostics"][k]["support"]==fold["test_classes"][k] for k in CLASSES)
            if r["mode"] == "grouped":
                assert fold["shared_active_regions"] == 0
            if r["mode"] == "chronological":
                assert "X" in fold["unrepresented_test_classes"]
                assert fold["thesis_style_ovr_bacc"] is None
            else:
                assert not fold["unrepresented_test_classes"]
        cases+=1
    assert cases==18, f"Expected 18 per-configuration JSON records, got {cases}"
    assert not json.loads((OUT / "failed_cases.json").read_text())
    print("PASS: source hash, split integrity, 18 model configurations, all confusion matrices,")
    print("      24 repeated-seed runs, 6 embargoed temporal runs, and missing-X safeguards.")

if __name__=="__main__":
    main()
