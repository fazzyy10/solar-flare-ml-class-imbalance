# Security and data handling

This repository is for academic review and reproducible research experiments, not a live service. It must never accept or publish client data, healthcare records, credentials, identifiable private files or unpublished employer configurations.

- Clone and inspect research code before running it. External Python packages and upstream datasets require normal due diligence.
- CI uses read-only repository permissions and a pinned external source URL, checked against the recorded Git blob and SHA-256 digests.
- No GitHub API token, storage key or cloud secret should be needed to reproduce these **public-source** experiments.
- Do not commit data under `local_data/`, generated experiment artifacts under `local_results/`, model pickle files, credentials or virtual environments.
- Report a suspected sensitive-data exposure **privately to the repository owner** rather than opening a public issue containing the material. GitHub private vulnerability reporting can be used when enabled; otherwise use the owner's verified private contact route.
- This project does not claim operational safety, cybersecurity certification or reliable real-time solar-flare alerts.

Dependencies are pinned to a previously executed Python 3.11 environment and recorded by a per-run freeze; they still require periodic vulnerability review.
