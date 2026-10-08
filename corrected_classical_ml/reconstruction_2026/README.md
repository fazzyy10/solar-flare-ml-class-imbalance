# DeepSun/FlareML data reconstruction — new post-MSc work (2026)

This directory adds an **independent, executable, post-MSc reconstruction pathway** for Fawaz's 2024 Data Science dissertation. It does **not** claim to contain the original assessed 2024 notebook, environment, or byte-identical local dataset, and it does not reproduce the dissertation's reported 29,400 model tests.

## Why this source?

The submitted thesis explicitly cites the DeepSun solar-flare prediction service at <https://nature.njit.edu/spacesoft/Flare-Predict/> and attributes its original SHARP dataset to the DeepSun research group. The corresponding public upstream research project is **[ccsc-tools/FlareML](https://github.com/ccsc-tools/FlareML)** by **Yasser Abduallah, Jason T. L. Wang and Haimin Wang**. The upstream project is distributed under the MIT licence (copyright 2021 Yasser Abduallah).

Source file: [`data/original_data/flaringar_original_data.csv`](https://github.com/ccsc-tools/FlareML/blob/44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c/data/original_data/flaringar_original_data.csv)

| Verified public source property | Value |
|---|---:|
| Rows | 845 |
| Distinct active-region IDs | 472 |
| SHARP numeric predictors | 13 |
| B / C / M / X | 128 / 552 / 142 / 23 |
| Columns including label, date and AR | 16 |
| Upstream commit | `44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c` |
| Git blob SHA-1 | `d3c40b44220b4480e0a600314cae46175cd9d127` |

**Important:** the public `flaringar_original_data.csv` contains **raw, differently scaled SHARP parameter values**. It is not itself a 0–1-normalised matrix. Some descriptions in the dissertation refer to normalised data, but that does not establish that a copy of this upstream raw CSV was the exact transformed input used for every submitted experiment.

## Quick start

From this directory:

```bash
python -m venv .venv
# activate .venv for your operating system
python -m pip install -r requirements.txt
python fetch_upstream.py
python experiment.py --mode stratified --model extra_trees --sampling none --output local_results/stratified_baseline.json
python experiment.py --mode grouped --model random_forest --sampling under --output local_results/grouped_under.json
python experiment.py --mode chronological --model extra_trees --sampling smote --output local_results/chronological_smote.json
python -m pytest -q
python sweep.py
python sweep_extensions.py
python -m jupyter nbconvert --to notebook --execute overview.ipynb --output overview-executed.ipynb
```

Downloading the dataset requires internet access. The fetch script pins the exact upstream commit, verifies Git's original file-content SHA-1, and prints a SHA-256 hash. The CSV is **not mirrored in this repository**. Files generated under `local_data/` and `local_results/` should remain uncommitted.

## What the code actually does

- Reads and validates the original reference schema and reported class distribution.
- Derives the four target labels (B/C/M/X) from upstream class-plus-intensity labels such as `X22`.
- Uses **13 source SHARP parameters** and retains active-region IDs and timestamps for split auditing.
- Fits scaling and optional random undersampling or SMOTE **inside the training fold** through an `imblearn.pipeline.Pipeline`.
- Provides two baseline classifiers: **Extra Trees** and **Random Forest**.
- Implements ordinary stratified 5-fold CV, stratified active-region grouped CV, or an 80/20 chronological holdout as separate **new 2026 evaluation options**.
- Separately reports scikit-learn macro recall and **the thesis-defined four-class one-vs-rest BACC/TSS**, calculated per class and averaged; scores are undefined for any test fold missing a flare class. The thesis's 2024 *experimental protocol* remains distinct despite matching metric definitions.
- Writes machine-readable JSON and CSV results **only when executed**. The verified 8 October 2026 outputs are summarised in [RESULTS_AND_LIMITATIONS_2026-10-08.md](RESULTS_AND_LIMITATIONS_2026-10-08.md), with full-precision GitHub Actions run artifacts.

**Important:** The initial 80/20 chronological test contains no X-class events and therefore cannot support a four-class BACC/TSS estimate. An explicitly exploratory 2014-date temporal sensitivity split is provided separately. Full methods and results: [8 October audit](RESULTS_AND_LIMITATIONS_2026-10-08.md).

## Boundaries and limitations

1. This is a **new post-MSc baseline**, not the original 14-classifier × resampled-dataset experiment.
2. Grouped validation is feasible here because the upstream original CSV includes `AR`, but grouped folds can change class distributions and must be interpreted cautiously.
3. Temporal evaluation is a chronological holdout, not evidence of operational deployment; dates correspond to upstream samples and their documented timestamp fields.
4. Fold-safe scaling and sampling are new safeguards and cannot be retroactively credited to the 2024 submission.
5. Exact experiment equivalence would require the original preprocessing steps, environment, seeds, source-file identity and complete submitted executable code, which have not been recovered.
6. The MIT-licensed *upstream software* remains credited to its authors. The Python modules here are written independently as new reconstruction code and do not copy upstream training scripts.

See the frozen submitted [dissertation text](../../submitted_msc_record/THESIS_FULL_TEXT.md), the root [provenance record](../../PROVENANCE.md) and the original [FlareML repository](https://github.com/ccsc-tools/FlareML) for the evidence hierarchy.