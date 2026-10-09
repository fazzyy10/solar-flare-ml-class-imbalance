# Solar-flare prediction: how much can we trust the evaluation?

**MSc Data Science research, Cardiff Metropolitan University**  
Mohamed Fawaz Hussain Fareed · Submitted 2024 · Further methodological work in 2026

[![Research workflow](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/workflows/deepsun-reconstruction.yml/badge.svg?branch=main)](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/workflows/deepsun-reconstruction.yml)

In my MSc dissertation, I investigated machine-learning approaches for predicting solar-flare classes using NOAA SHARP magnetic parameters. The difficulty was not simply getting a classifier to recognise patterns. The data were severely imbalanced: out of **845 recorded flare events**, only **23 were X-class**, the rarest and most intense class in the dataset.

I compared different classical ML algorithms and sampling methods, including random undersampling and SMOTE. At the time, the main question was which approach gave the strongest results when the classes were so uneven.

When I revisited the work after graduating, I was interested in something more specific. Several of the events come from the **same solar active region**. If observations from one region appear in both the training and validation sets, what exactly are we testing? It might be a useful result for a random event split, but it does not necessarily tell us how a model will handle a region it has never encountered.

That question led to the separate, executable **2026 evaluation study** in this repository.

[My research discussion](docs/RESEARCH_REVIEWER_GUIDE.md) · [Detailed 2026 results](corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) · [Run the experiments](corrected_classical_ml/reconstruction_2026/) · [Read my submitted dissertation](submitted_msc_record/THESIS_FULL_TEXT.md)

![Class distribution in the public reference dataset](docs/figures/class_imbalance.svg)

## The original MSc study

My assessed dissertation, *Application of Machine Learning Modeling in NOAA SHARP Data for Solar Flare Prediction*, compared **14 classifiers** using the dissertation's evaluation and sampling procedures.

It reported **Extra Trees** as the leading classifier, with an average **Balanced Accuracy (BACC) of 0.829979** and **True Skill Statistic (TSS) of 0.659958**, calculated using the thesis's one-versus-rest definitions.

These are the figures **reported in the 2024 dissertation**. I cannot claim an exact numerical reproduction of that study because the original executable workflow and its complete preprocessing state have not been recovered. There is also an unresolved discrepancy between the test count stated in the dissertation (**29,400**) and the number implied by its described combinations (**28,140**). Both the assessed text and the explanation of that discrepancy are available in [the submitted-methods record](docs/METHODS_SUBMITTED.md).

## What changed when I tested active regions separately?

The public reference dataset contains **472 active regions**, and **206** of them appear in more than one event. The later pipeline compares conventional stratified cross-validation with validation that keeps active regions on separate sides of the split. Scaling and optional resampling take place within each training fold.

![Comparison of stratified, active-region-grouped and chronological evaluation](docs/figures/validation_comparison.svg)

One example from the new work is Extra Trees with SMOTE applied within the training folds:

| Five-fold evaluation | Four-class one-versus-rest BACC |
|---|---:|
| Stratified event-level split | **0.7071** |
| Active-region-grouped split | **0.6413** |

In the wider three-seed analysis, grouped scores were lower in **17 of 18 matched comparisons**. This is an important sensitivity result, although the score difference cannot be attributed entirely to leakage. Grouped folds also change which examples and flare classes appear in each test set.

The chronological experiment raised a different problem. The final 20% of events by date contains **no X-class flares**. I cannot report a valid four-class BACC or TSS for that test. A separate cutoff starting in 2014 contains nine X-class test examples, but that date was chosen after inspecting the original split and remains a **post-hoc sensitivity check**.

There is a further limitation to the underlying data. These are curated *flare-event* records, without the quiet periods needed to measure operational false alarms. The exact lead time from the magnetic observations to each flare has not been independently verified either. The repository therefore does not demonstrate a working 24-hour operational forecasting service.

[Read the complete protocol, split diagnostics and numerical results](corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md).

## How to examine the work

The submitted 2024 dissertation, the independent 2026 code and the upstream FlareML project have different origins. I have kept them separate so that the methods and the results can be checked without confusing their authorship or dates.

| Material | Purpose |
|---|---|
| [Submitted dissertation](submitted_msc_record/THESIS_FULL_TEXT.md) | Full-text record of the assessed 2024 research |
| [Research questions](docs/RESEARCH_QUESTIONS.md) and [submitted methods](docs/METHODS_SUBMITTED.md) | What I originally set out to test |
| [2026 code, tests and notebook](corrected_classical_ml/reconstruction_2026/) | The independently developed follow-up evaluation |
| [Results and limitations](corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) | Experimental settings, fold issues and verified findings |
| [Permanent result tables](results/2026-10-08/) | Machine-readable outputs retained in the repository |
| [Dataset card](data/DATASET_CARD.md) and [model card](docs/MODEL_CARD_2026.md) | Source, intended use and methodological limits |
| [Provenance](PROVENANCE.md) and [upstream comparison](docs/UPSTREAM_COMPARISON.md) | Research ownership and comparison with the original software |

For the new code, use Python 3.11 and run:

```bash
cd corrected_classical_ml/reconstruction_2026
python -m pip install -r requirements.txt
python -m pytest -q
python fetch_upstream.py
python sweep.py
python sweep_extensions.py
```

The source CSV is fetched from a **pinned public FlareML revision** and verified with its published hashes; it is not redistributed. The notebook, repeated-seed experiments and validation scripts are also executed by [GitHub Actions](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/workflows/deepsun-reconstruction.yml).

## What I would investigate next

With more time and an independently selected dataset, I would want to know whether the same conclusions survive a prospectively fixed temporal split, other solar cycles and different active regions. I would also examine calibration and uncertainty for X-class predictions. With only 23 X events in this reference dataset, the uncertainty deserves as much attention as the mean score.

The original **DeepSun/FlareML** software and data source belong to **Yasser Abduallah, Jason T. L. Wang and Haimin Wang**. I acknowledge their [public repository](https://github.com/ccsc-tools/FlareML) and [archived release](https://doi.org/10.5281/zenodo.5634114). My dissertation and the later evaluation code do not make me the author of their system. The 2026 follow-up is unpublished and has not undergone peer review.

---

**Related research:** [BSc study of mobile navigation-system acceptance in Sri Lanka](https://github.com/fazzyy10/bsc-driver-acceptance-navigation)  
*Mohamed Fawaz Hussain Fareed · Cardiff, United Kingdom*
