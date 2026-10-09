# A closer look at the solar-flare experiments

**MSc Data Science, Cardiff Metropolitan University**  
2024 dissertation and a separate methodological investigation carried out in 2026

## The problem I was trying to solve

My MSc work used NOAA SHARP magnetic parameters to classify solar-flare events as B, C, M or X. The original dataset has **845 events** and only **23 X-class events**. Because of that imbalance, I did not want ordinary accuracy to be the only basis for model comparison.

The submitted dissertation investigated 14 machine-learning classifiers and different data-sampling methods. It reported Extra Trees as the strongest overall performer under the thesis's evaluation protocol, with **BACC 0.829979** and **TSS 0.659958**. Those numbers come from the **2024 assessed study**. I have not recovered the complete original executable setup needed to reproduce them exactly.

[Read the assessed dissertation](../submitted_msc_record/THESIS_FULL_TEXT.md) or [its reported methods](METHODS_SUBMITTED.md).

## Revisiting the validation design

The point I wanted to check in 2026 was whether random event-level validation answered the right question.

There are **472 active regions** in the reference data, with **206 regions contributing repeated events**. If a model sees a region during training and is then tested on another event from the same region, that may be easier than predicting a flare from an entirely unseen region.

The separate 2026 pipeline keeps active regions apart in grouped validation, fits preprocessing within training folds, and compares results with conventional stratified splits. That later analysis is [available as executable code](../corrected_classical_ml/reconstruction_2026/).

![Comparison of validation approaches](figures/validation_comparison.svg)

For Extra Trees with train-fold SMOTE, the new five-fold study returned these mean four-class one-versus-rest BACC values:

| Split | BACC |
|---|---:|
| Stratified | **0.7071** |
| Grouped by active region | **0.6413** |

Across three random seeds and the model/sampling combinations, the grouped BACC was lower in **17 of 18 matched settings**.

I would not interpret that entire difference as leakage. Grouping alters fold membership and class composition as well as preventing the same region from appearing on both sides of a split. Still, it changes the evaluation enough that I would want the intended deployment question settled *before* choosing the split.

## When a score should be left undefined

The first chronological experiment trained on the earliest 80% of events and tested on the final 20%. There were **no X-class flares** in that test period, so it could not give a meaningful four-class BACC or TSS.

I explored an alternative cutoff beginning in 2014 with nine X-class test examples. I chose it after seeing the first problem. It is therefore **post hoc** and cannot be treated as a clean external test.

There is also a limit to the upstream data itself. They contain curated flare-event observations, not all the quiet periods when no flare occurs. Such a dataset cannot establish the real-world false-alarm rate of a forecasting service. The required lead time between magnetic features and labelled flare events is not independently verified in this repository.

## A separate issue in the assessed record

The 2024 dissertation reports **29,400 model tests**. The procedure described in the dissertation implies **201 dataset variants × 10 folds × 14 classifiers = 28,140**. I do not have an original run log that resolves the difference, and I have not revised the historical submission. The number 29,400 remains a *reported* figure rather than a confirmed execution count. [Details](METHODS_SUBMITTED.md).

Similarly, the archived `ccsc_FlareML.ipynb` entry turned out to be an HTML snapshot of an upstream page, not a complete runnable notebook. I have not treated it as recovered 2024 executable code.

## Where the new evidence can be checked

The 2026 pipeline uses the pinned public upstream CSV, verifies its bytes, and records active-region overlap and class support by fold. Its outputs include class-level diagnostics and confusion matrices, as well as the reported aggregate scores.

[2026 results and experimental settings](../corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) · [Source code](../corrected_classical_ml/reconstruction_2026/experiment.py) · [Tests](../corrected_classical_ml/reconstruction_2026/test_reconstruction.py) · [GitHub Actions scientific run](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37918912141)

The next experiment I would design is a prospectively fixed temporal evaluation, with independent data and clear uncertainty estimates around the rare X class. I would keep any model selection separate from the final evaluation.

The **2024 thesis** and the **2026 study** answer related but different questions. This repository records what I reported in the degree, what I subsequently tested, and which conclusions the evidence still does not support.

**Source credit:** the original DeepSun/FlareML research software and data were developed by **Yasser Abduallah, Jason T. L. Wang and Haimin Wang**. [Upstream repository](https://github.com/ccsc-tools/FlareML) · [Ownership and source details](UPSTREAM_COMPARISON.md) · [Dataset card](../data/DATASET_CARD.md). The 2026 investigation is not a peer-reviewed paper or a deployed space-weather forecast system.
