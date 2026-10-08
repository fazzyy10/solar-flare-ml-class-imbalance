"""Check public authored documentation links and research source boundaries."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import unquote
import re

ROOT = Path(__file__).resolve().parents[2]
DOCUMENTS = [
    ROOT / "README.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "CHANGELOG.md",
    *sorted((ROOT / "docs").glob("*.md")),
    ROOT / "data" / "DATASET_CARD.md",
    ROOT / "results" / "2026-10-08" / "README.md",
    ROOT / "corrected_classical_ml" / "reconstruction_2026" / "README.md",
]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def check() -> list[str]:
    errors = []
    for source in DOCUMENTS:
        if not source.is_file():
            errors.append(f"Missing expected document: {source.relative_to(ROOT)}")
            continue
        for match in LINK.finditer(source.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0].split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("http:", "https:", "mailto:", "data:", "/")):
                continue
            local = (source.parent / unquote(target)).resolve()
            if not local.is_relative_to(ROOT.resolve()) or not local.exists():
                errors.append(f"{source.relative_to(ROOT)} -> broken link: {target}")
    return errors

if __name__ == "__main__":
    problems = check()
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Research documentation link audit passed ({len(DOCUMENTS)} files).")
