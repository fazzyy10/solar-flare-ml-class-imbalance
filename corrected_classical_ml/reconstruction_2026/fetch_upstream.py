"""Fetch the public DeepSun/FlareML reference CSV without redistributing it."""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

UPSTREAM_COMMIT = "44ffd7ad0a6945ee36f6e488a034b8266cb4fb4c"
UPSTREAM_PATH = "data/original_data/flaringar_original_data.csv"
GIT_BLOB_SHA1 = "d3c40b44220b4480e0a600314cae46175cd9d127"
EXPECTED_SHA256 = "69c36526144f5d1485b7f8cc55b254c857c885a840020fe3cb2b887f4c4f8cd3"
URL = f"https://raw.githubusercontent.com/ccsc-tools/FlareML/{UPSTREAM_COMMIT}/{UPSTREAM_PATH}"


def verify_git_blob(payload: bytes) -> bool:
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest() == GIT_BLOB_SHA1


def download(destination: Path) -> tuple[Path, str]:
    request = Request(URL, headers={"User-Agent": "MSc-FlareML-reconstruction/1.0"})
    with urlopen(request, timeout=30) as response:
        payload = response.read()
    if hashlib.sha256(payload).hexdigest() != EXPECTED_SHA256:
        raise ValueError("Public source failed the recorded SHA-256 integrity check")
    if not verify_git_blob(payload):
        raise ValueError("Upstream file failed the pinned Git blob SHA-1 integrity check")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return destination, hashlib.sha256(payload).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "local_data" / "flaringar_original_data.csv")
    args = parser.parse_args()
    path, checksum = download(args.output)
    print(f"Source: {URL}")
    print(f"Saved: {path}")
    print(f"SHA-256: {checksum}")
    print(f"Verified upstream Git blob SHA-1: {GIT_BLOB_SHA1}")


if __name__ == "__main__":
    main()
