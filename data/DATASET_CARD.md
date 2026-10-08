# Dataset card — public DeepSun / FlareML SHARP event sample

**Source authors:** Yasser Abduallah, Jason T. L. Wang and Haimin Wang, not this repository's owner.

**Source of the data:** [ccsc-tools/FlareML](https://github.com/ccsc-tools/FlareML), `data/original_data/flaringar_original_data.csv`, commit `44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c`.

**Integrity:** Git blob SHA-1 `d3c40b44220b4480e0a600314cae46175cd9d127`; SHA-256 `69c36526144f5d1485b7f8cc55b254c857c885a840020fe3cb2b887f4c4f8cd3`. Data are fetched on demand and **not copied into this repository**. Do not assume that this was the byte-identical post-processing input used locally in 2024.

## Unit and population

One row represents one curated solar-flare event associated with one solar active region. There are **845** event rows and **472** active regions spanning May 2010–December 2016. The label is a four-class reduction of the upstream `Flare Class` field (B, C, M or X), removing the intensity suffix.

| Class | Events | Approximate prevalence |
|---|---:|---:|
| B | 128 | 15.1% |
| C | 552 | 65.3% |
| M | 142 | 16.8% |
| X | 23 | 2.7% |

**206** active-region IDs occur in multiple rows; no active region has different B/C/M/X labels in this particular source. Because events from a common region are dependent, random event-level splits do not necessarily represent forecasting for entirely unseen regions.

## Schema and features

Metadata: `Flare Class` (original category and intensity code), `Flare Date` (event timestamp string), `AR` (active-region identifier). These metadata fields **are not model predictors**.

13 numerical SHARP-derived magnetic predictors: `TOTUSJH`, `TOTBSQ`, `TOTPOT`, `TOTUSJZ`, `ABSNJZH`, `SAVNCPP`, `USFLUX`, `AREA_ACR`, `TOTFZ`, `MEANPOT`, `R_VALUE`, `EPSZ`, `SHRGT45`.

The upstream source contains **raw-scale numerical values**, including different physical orders of magnitude. The 2026 code fits the scaler on training folds; the original MSc dissertation also discusses normalisation, but the precise historical transformation cannot be reconstructed from this source alone.

## Intended research uses

- Comparison of classification baselines under severe class imbalance.
- Evaluation-design studies: stratified event-level CV, active-region-grouped CV and chronological separation.
- Demonstrating provenance, source integrity and reproducibility of a **new 2026 research exercise**.

## Restrictions and limitations

- Small rare-X sample: only 23 total X events, so per-class estimates are fragile.
- Observational, curated event-only sample; not a representative time-continuous operational alert stream. Absence of flare events and false alarms in quiet periods are not modeled.
- AR groups are repeated; random folds can share regions. Test the AR-separation assumptions explicitly.
- The naive last-20% chronological holdout contains **zero X-class events**; its four-class TSS/BACC is undefined.
- Dataset selection procedures, timestamp semantics, external validity, observation delays and deployment eligibility are not independently revalidated here.
- No persons, clients or confidential employer data are used.

## Data rights and citation

The FlareML software has an MIT licence; **do not infer automatically that every dataset has unrestricted redistribution rights**. This project links to and fetches publicly accessible data, without sublicensing or claiming creation of the underlying observations. Cite the upstream team and publications (see root `LICENSES_AND_ATTRIBUTION.md`) and distinguish their dataset from later analysis.

## Reproduce the inspection

```bash
cd corrected_classical_ml/reconstruction_2026
python -m pip install -r requirements.txt
python fetch_upstream.py
python sweep.py
```

Inspect `local_results/data_profile.json` and `local_results/split_diagnostics.json`. The [2026 research results](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) include class-level and split-level limitations.
