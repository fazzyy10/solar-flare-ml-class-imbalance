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
    *sorted((ROOT / "submitted_msc_record").glob("*.md")),
    ROOT / "data" / "DATASET_CARD.md",
    ROOT / "results" / "2026-10-08" / "README.md",
    ROOT / "corrected_classical_ml" / "reconstruction_2026" / "README.md",
]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

def check_thesis_presentation() -> list[str]:
    """Protect the submitted dissertation's panel-facing reading edition."""
    errors = []
    folder = ROOT / "submitted_msc_record"
    reading = folder / "THESIS_FULL_TEXT.md"
    archive = folder / "THESIS_SOURCE_EXTRACTION_ARCHIVE.md"
    if not reading.is_file() or not archive.is_file():
        return ["Submitted thesis reading copy or immutable extraction archive is missing"]
    text = reading.read_text(encoding="utf-8")
    raw = archive.read_text(encoding="utf-8")
    if len(text) < 100_000 or len(raw) < 110_000:
        errors.append("MSc submitted full-text record is unexpectedly truncated")
    if re.search(r"\\d+\\s*\\|\\s*P\\s*a\\s*g\\s*e", text, flags=re.I):
        errors.append("Stray source-PDF page marker remains in formatted thesis")
    for chapter in range(1, 7):
        if f"## Chapter {chapter}:" not in text:
            errors.append(f"Missing MSc thesis chapter {chapter}")
    for number in range(1, 25):
        if f"View Figure {number} in the original dissertation" not in text:
            errors.append(f"Missing submitted-PDF link for figure {number}")
    if "1zzil6swde2hxFKjo_YA_aFCiNSIZMD8N" not in text:
        errors.append("Missing authoritative source-PDF link")
    return errors

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
    errors.extend(check_thesis_presentation())
    return errors

if __name__ == "__main__":
    problems = check()
    if problems:
        raise SystemExit("\n".join(problems))
    print(f"Research documentation link audit passed ({len(DOCUMENTS)} files).")
