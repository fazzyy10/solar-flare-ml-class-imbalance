# Contributing to this research record

This repository combines immutable historical academic evidence and a separate 2026 modelling audit. Contributions are welcome when they improve source verification, code quality, reproducibility or scientific interpretation **without rewriting the submitted 2024 dissertation**.

## Research evidence and ownership rules

- **Do not edit** `submitted_msc_record/` or the 2024 thesis text to fix historical methodology. Submit a separate correction or explanatory note in `reproducibility_audit/` or `docs/` with evidence.
- Public DeepSun/FlareML source data and code are the work of their upstream authors. Cite sources and respect licences. The dataset is not redistributed here.
- 2026 numerical claims must point to a reproducible command, verified source bytes, environment and associated machine-readable result.
- No employer, client, healthcare, PHI, credentials, private worksheets or third-party academic submissions.
- Proposed scientific changes should state whether an outcome is **historical**, **newly verified**, **hypothetical**, or **not independently tested**.

## Local checks

Use Python 3.11 and the pinned dependencies in `corrected_classical_ml/reconstruction_2026/requirements.txt`:

```bash
cd corrected_classical_ml/reconstruction_2026
python -m pip install -r requirements.txt
python -m pytest -q
python -m compileall -q experiment.py fetch_upstream.py sweep.py sweep_extensions.py
python check_repo_quality.py
```

For changes that affect scientific results, additionally run `python fetch_upstream.py`, `python sweep.py`, `python sweep_extensions.py` and the notebook. Pull requests should describe *what changed*, the validation protocol, numerical difference from the previous commit where applicable, and any new limitation.

## Review standard

Keep the README concise, links working, scripts runnable from a clean environment and source-to-claim boundaries explicit. This project is a research record, **not** a replacement for DeepSun's service or a source of operational space-weather predictions.
