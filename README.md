# When the rarest events matter most

### Solar-flare classification, class imbalance and the way we test a model

**Mohamed Fawaz Hussain Fareed**  
MSc Data Science (Distinction), Cardiff Metropolitan University · 2024 dissertation  
Independent methodological investigation · 2026

[![Verified research checks](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/workflows/deepsun-reconstruction.yml/badge.svg?branch=main)](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/workflows/deepsun-reconstruction.yml)

A model can achieve an impressive average score while telling us very little about the events we most want to identify. This is the problem that drew me to solar-flare prediction for my MSc dissertation.

The research used NOAA SHARP magnetic parameters to classify B, C, M and X solar flares. But out of **845 labelled events, only 23 were X-class**. If we evaluate every class as though it has the same amount of evidence behind it, it is easy to come away with more confidence than the data warrant.

I initially approached this as a problem of **class imbalance and model comparison**. Coming back to the work later, I found another question just as important: **what counts as an independent test of a solar-flare model?**

[Read the research note](docs/RESEARCH_REVIEWER_GUIDE.md) · [Inspect the results](corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) · [Run the code](corrected_classical_ml/reconstruction_2026/) · [Read the submitted dissertation](submitted_msc_record/THESIS_FULL_TEXT.md)

![Distribution of B, C, M and X solar flare events from the referenced public dataset](docs/figures/class_imbalance.svg)

## The dissertation: a question about imbalance

My assessed MSc study, *Application of Machine Learning Modeling in NOAA SHARP Data for Solar Flare Prediction*, compared **14 classical machine-learning classifiers** and investigated sampling approaches including random undersampling and SMOTE.

The submitted thesis reports **Extra Trees** as its leading method with average **BACC = 0.829979** and **TSS = 0.659958**, using the thesis's metric definitions and reported experimental aggregation. Those are **the 2024 dissertation's reported results**, not numbers this repository claims to have reproduced exactly. The original full executable notebook and preprocessing environment have not been recovered in a form that would justify that claim.

The original research is [preserved in full text](submitted_msc_record/THESIS_FULL_TEXT.md); [its evidence and authorship boundaries](PROVENANCE.md) are recorded separately. I have not rewritten the assessed research to make it appear more current.

## The question I came back to

The reference data contain **472 solar active regions**. Some regions contribute more than one flare event. In fact, **206 regions occur repeatedly**.

If a conventional random stratified split places observations from the *same active region* on both sides of a fold, how much does that validation resemble predicting flares from a region the model has never seen?

That prompted a separate **2026 investigation**, written and executed after the MSc. It does not replace the submitted study. It tests Extra Trees and Random Forest with training-fold-safe preprocessing and compares ordinary stratified folds, active-region-separated folds and chronological tests.

![Stratified, region-grouped and temporal evaluation designs](docs/figures/validation_comparison.svg)

Here is a concrete example from the new runs:

| Extra Trees with training-fold SMOTE | Four-class one-vs-rest BACC |
|---|---:|
| Stratified five-fold validation | **0.7071** |
| Active-region-grouped five-fold validation | **0.6413** |

For the broader repeated-seed comparison, the grouped score was lower in **17 of 18 matched settings**. I would **not** call the difference a measured leakage effect: grouping changes which observations appear in each fold as well as preventing active-region overlap. The result shows that the evaluation choice matters. It does not isolate one cause.

There was another useful warning. The simple final-20%-by-time holdout contains **no X-class events**. A full four-class BACC or TSS is therefore undefined, no matter how attractive the remaining numbers might look. A separately labelled *post-hoc* temporal sensitivity check is documented, but it is not a substitute for a prospectively chosen external test.

These may look like inconvenient findings. To me, they are the most interesting part of the continued research.

## Look at the evidence

I wanted this to be inspectable rather than just a PDF and a strong-looking result:

| What you want to check | Where to look |
|---|---|
| The actual question and the meaning of the results | [Research review](docs/RESEARCH_REVIEWER_GUIDE.md) |
| The original assessed MSc study | [Submitted dissertation](submitted_msc_record/THESIS_FULL_TEXT.md) |
| The separately implemented 2026 models, tests and notebook | [Reconstruction code](corrected_classical_ml/reconstruction_2026/) |
| The 18 model configurations, 24 repeat-seed runs and six exploratory temporal checks | [Detailed results](corrected_classical_ml/reconstruction_2026/RESULTS_AND_LIMITATIONS_2026-10-08.md) |
| Source data identification and restrictions | [Dataset card](data/DATASET_CARD.md) |
| Evaluation metrics and intended-use limits | [Model card](docs/MODEL_CARD_2026.md) |
| Results that remain available after CI artifacts expire | [Permanent results](results/2026-10-08/) |
| Exact provenance, what was originally submitted, what was added later | [Research provenance](PROVENANCE.md) |
| How this differs from the upstream research | [DeepSun/FlareML comparison](docs/UPSTREAM_COMPARISON.md) |
| Remaining reproducibility questions | [Research checklist](docs/REPRODUCIBILITY_CHECKLIST.md) |

To run the later code locally:

```bash
cd corrected_classical_ml/reconstruction_2026
python -m pip install -r requirements.txt
python -m pytest -q
python fetch_upstream.py
python sweep.py
```

The input is downloaded from a **pinned public version** of FlareML and its bytes are checked; raw data are not redistributed here. GitHub Actions runs the tests, modelling sweeps and notebook. The [successful workflow](https://github.com/fazzyy10/solar-flare-ml-class-imbalance/actions/runs/37831563054) provides evidence that the 2026 analysis executed, **not** that the exact 2024 experiment has been replicated.

## Credit where it belongs

The **FlareML/DeepSun** reference project and source software were developed by **Yasser Abduallah, Jason T. L. Wang and Haimin Wang**. Their [public project](https://github.com/ccsc-tools/FlareML) and [archived release](https://doi.org/10.5281/zenodo.5634114) are acknowledged throughout this repository. I do not claim their system, publications or data collection as my own work.

The 2026 analysis is a new, narrower investigation into evaluation methodology. It is **unpublished**, not a peer-reviewed contribution, not an operational space-weather forecasting system and not evidence that my models outperform DeepSun in deployment.

## Where I would take this next

I would want independent data and a prospectively fixed time split, stronger uncertainty estimates around the X class, and tests of what survives across regions or solar cycles. I would also want to separate model selection from the final test entirely.

The question I now find most useful is not simply *which classifier has the highest score?* It is *what would need to be true for me to trust that score?*

---

**Other research:** [BSc — driver acceptance of mobile navigation systems in Sri Lanka](https://github.com/fazzyy10/bsc-driver-acceptance-navigation)  
**About:** Mohamed Fawaz Hussain Fareed · Cardiff, United Kingdom · Data Analytics, Business Analysis, Process Improvement and Applied Data Science
