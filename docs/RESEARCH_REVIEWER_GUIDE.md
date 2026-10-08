# Research review | Solar-flare prediction under class imbalance

**Mohamed Fawaz Hussain Fareed — MSc Data Science, Cardiff Metropolitan University (2024)**  
**Research record and transparent post-MSc methodological investigation (2026)**

This repository contains two deliberately different pieces of work. The assessed MSc dissertation studied four-class solar-flare prediction using NOAA SHARP-derived magnetic parameters. The later follow-up interrogates the original evaluation assumptions using an independently implemented classical-ML pipeline and the publicly available source dataset. It does **not** rewrite the submitted study.

## The research question

**What changes when solar-flare models are evaluated on previously unseen active regions, instead of randomly partitioning events from the same region?**

The public data contain 845 labelled events from 472 active regions, with only 23 X-class events. Of 472 regions, 206 have multiple events. This makes ordinary stratified cross-validation a useful conventional baseline, but potentially optimistic for a new-region generalisation question.

## Reproducible evidence

| Item | Evidence |
|---|---|
| Original dissertation | [Complete submitted thesis text](../submitted_msc_record/THESIS_FULL_TEXT.md) · [submission provenance](../PROVENANCE.md) |
| Public research source | [FlareML](https://github.com/ccsc-tools/FlareML) by Abduallah, J. T. L. Wang and H. Wang |
| Exact input version | Git commit `44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c`, data SHA-256 `69c36526144f5d1485b7f8cc55b254c857c885a840020fe3cb2b887f4c4f8cd3` |
| New executable analysis | [Code, tests and notebook](../corrected_classical_ml/reconstruction_2026/) |
| Verified execution | [GitHub Actions scientific audit](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37823855291) |
| Methods and detailed results | [2026 results and limitations](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) |

## Findings worth discussing at a research interview

1. **Dependence between events matters.** In ordinary stratified CV, some active-region identifiers appear in both train and validation folds (88–93 per fold in the seed-42 audit). Grouped CV eliminates those overlaps.
2. **The evaluation design changes the result.** For Extra Trees with train-fold-only SMOTE, thesis-style mean one-versus-rest BACC is **0.7071** in stratified CV and **0.6413** in grouped CV. Scores should not be interpreted as a measured causal leakage bias: grouping also changes the composition and difficulty of the folds.
3. **Extreme events remain fragile.** A naive final-20%-by-time holdout has zero X-class events. Thus its full four-class BACC/TSS is undefined. A *post-hoc* 2014-start split contains nine X-class examples after an active-region embargo, but is too small and retrospectively chosen to support an operational forecasting claim.
4. **Metric definitions matter.** The dissertation's four one-versus-rest BACC/TSS values are averaged, rather than using scikit-learn's ordinary multiclass balanced accuracy (macro recall). The repository records both under separate names.
5. **Reproduction is not the same as reinterpretation.** The submitted 2024 thesis reports Extra Trees BACC 0.829979 and TSS 0.659958; its original executable notebook and complete preprocessing state were not recovered. Different folds, hyperparameters, sampling frequencies and source transformations prevent a like-for-like numerical comparison.

## Why this is relevant to ML doctoral research

The useful transferable practice is **asking whether an evaluation measures the scientific question it claims to measure**. That question carries into time-series forecasting, probabilistic modelling, uncertainty quantification and distribution shift. It also creates tractable next experiments: grouped versus time-blocked splits, uncertainty estimates for rare classes, model-selection separation, calibration and external validation.

This project **does not claim** proficiency in probabilistic forecasting, advanced GNNs, peer-reviewed publication, or deployed space-weather services. It demonstrates an MSc ML research base and a later, critical, reproducible examination of its assumptions.

**Suggested reading order (under five minutes):** [data and validation figure](figures/validation_comparison.svg) → this page → [results](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) → [code](../corrected_classical_ml/reconstruction_2026/experiment.py) → thesis methodology.

*This reviewer guide supplements the frozen Hildesheim application documents; it does not replace or revise them.*
