# Benchmark against established scientific ML repository practices

Reviewed 8 October 2026. This comparison is **architectural**, not a model-performance leaderboard. We use independent practices and cite their authors rather than copying source files from other projects.

## Exemplars and what was learned

| Example | Relevant strengths actually visible | Adopted here | Deliberate boundary |
|---|---|---|---|
| [DeepSun/FlareML](https://github.com/ccsc-tools/FlareML) | Published domain software, dataset folders, notebooks, forecasting models, environment and external release/DOI | Pinned upstream data, executable notebook, several model evaluations, source credits | We cannot claim parity with forecasting service, published research, or upstream four-method ensemble |
| [Papers with Code ML research-code guide](https://github.com/paperswithcode/releasing-research-code) | Code completeness: dependencies, training, evaluation, weights where appropriate, results and commands | Concrete commands, pinned versions, training/evaluation, results tables, data/model cards | Weights are not shared because the objective is validation research, not a deployed model |
| [Cookiecutter Data Science](https://github.com/drivendataorg/cookiecutter-data-science) | Consistent project layout, clear source versus generated data separation, testing and documentation | `local_data/`/ `local_results/` ignored; named scripts, research docs, explicit inputs/outputs | We did not blindly import an enterprise project scaffold |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Automated checks, tests, contribution policy, citation, security and maintenance practices | Tests, CI, CONTRIBUTING, SECURITY, source checker, reviewer-facing links | This small research project does not claim a comparable library or maintenance organisation |
| [NeurIPS reproducibility guidance](https://neurips.cc/public/guides/PaperChecklist) | Reproducible claims, exact experimental conditions, data/code provenance and honest limitations | [Traceable evidence checklist](REPRODUCIBILITY_CHECKLIST.md), source checksum and limitations | Not an officially reviewed or published NeurIPS result |

## What has improved beyond the original FlareML packaging for *this distinct research purpose*

For the narrower question of **evaluation auditability**, this project now includes explicit train/test active-region overlap diagnostics, fold-level four-by-four confusion matrices and class support, missing-class guards, independent data SHA-256 plus Git blob checks, and published limitations for a chronological test with no X-class events. These are useful features of **this** repository; they are **not** grounds for claiming that the MSc study or a 2026 Extra Trees model beats DeepSun's forecast system.

## Further research that remains genuinely incomplete

1. Statistical uncertainty: bootstrap/group-aware intervals or repeated-group designs with predeclared estimands; current three seeds are descriptive.
2. External validity: independently curated space-weather sources, fully prospective temporal holdout, no optimization on the test split.
3. Comparative scope: reproduce the original 14 classifier environment and 100 sampling variants only if the actual archive is recovered.
4. Model safety: calibration, event-time correctness, quiet-period false-alarm rates and operational alert performance.
5. Sustainability: an archived, immutable versioned public release/DOI if and when a stable research software release is approved.
6. Model artifacts: public checkpoints only when their purpose, ownership, security and lineage can be verified.

A repository can lead on *clarity and reproducibility of claims* without replacing more advanced upstream research or inventing new scientific contributions.

## Source-to-claim hierarchy

1. 2024 frozen submitted thesis and official academic record.
2. Actual 2026 model runs with verifiable GitHub Actions and source hash.
3. Documentation derived from those verified sources.
4. Ideas and future-work proposals, always labelled untested.

This protects both the original dissertation and future PhD-application evidence.
