# Research-code reproducibility and transparency checklist

The scope here is the independently developed **2026 baseline experiment**, not the original 2024 dissertation code. Inspired by [Papers with Code's ML Code Completeness Checklist](https://github.com/paperswithcode/releasing-research-code) and [NeurIPS paper guidance](https://neurips.cc/public/guides/PaperChecklist). This is a **self-audit**, not a formal conference certification.

| Criterion | Status | Evidence and limits |
|---|---|---|
| State research question and purpose | Yes | [Five-minute reviewer guide](RESEARCH_REVIEWER_GUIDE.md) |
| Source and dataset version | Yes | [Dataset card](../data/DATASET_CARD.md), commit and Git/SHA256 hashes |
| Executable model training | Yes, for 2026 scope | [Python baselines](../corrected_classical_ml/reconstruction_2026/experiment.py) |
| Runnable evaluation | Yes, for 2026 scope | [Sweep code](../corrected_classical_ml/reconstruction_2026/sweep.py) and extensions |
| Evaluation of rare classes | Partial | Fold-level metrics, confusion matrices and missing-X guards; X sample small |
| Environment description | Yes | Python 3.11 + pinned direct versions + pip-freeze output per CI run; transitive lock not yet maintained in Git |
| Train/test data isolation | Yes, for reviewed code | Fold-safe sampling and AR-grouping assertions |
| Chronological evaluation | Partial | 80/20 holdout lacks X; alternative cutoff is post hoc |
| Machine-readable results | Yes | [Permanent CSV summaries](../results/2026-10-08/) and CI full run artifacts; detailed artifacts expire |
| Stable performance uncertainty | No | Three seeds are descriptive, not inference or confidence intervals |
| Prospectively locked external test | No | No independent dataset tested |
| Pretrained model weights | Not applicable | Focus is training-and-validation protocol, not model deployment; retraining is supported |
| Replication of submitted 2024 experiment | No | Original code, seeds, transformations and full environment not recovered |
| Model/data intended use and limits | Yes | [Model card](MODEL_CARD_2026.md) and [dataset card](../data/DATASET_CARD.md) |
| Peer review / publication | No | Assessed MSc and unpublished follow-up |
| Client/patient/private data release | Not applicable | None used or distributed |

## Commands

```bash
cd corrected_classical_ml/reconstruction_2026
python -m venv .venv
# Activate venv, then:
python -m pip install -r requirements.txt
python -m pytest -q
python fetch_upstream.py
python sweep.py
python sweep_extensions.py
python -m jupyter nbconvert --to notebook --execute overview.ipynb --output overview-executed.ipynb --output-dir local_results
```

The last command executes figures and analysis, using locally generated CSVs. Results and environment manifests are recorded under `local_results/`, which is ignored in Git. CI executes these checks on GitHub-hosted Python 3.11. Published [2026 result tables](../results/2026-10-08/) are the permanent subset.

## Known research questions for a follow-up

- Is true leave-active-region-out forecasting generalisable across solar cycles?
- How does grouping affect class support and statistical uncertainty, especially X?
- How do prospective chronological test design and source selection differ from post-hoc selection?
- Do alternative performance definitions and priors change the interpretation?
- Can an external dataset and locked model-selection protocol support independently validated conclusions?

**Do not mark these questions as solved or represented as new academic publications.**
