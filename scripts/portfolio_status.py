#!/usr/bin/env python3
"""Portfolio status and consistency check (stdlib only).

Counts requirements, test cases, bugs and AI-log rows; finds TODO/EXAMPLE placeholders;
checks that every automated test points to a real test case, and every test case to a real
requirement; prints confidence calibration when there are enough rows.

Exit code 1 on errors (orphan references). With --strict, placeholders also fail.
Usage: python scripts/portfolio_status.py [--strict]
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQ_RE = re.compile(r"\bREQ-[A-Z]+-\d+\b")
TC_RE = re.compile(r"\bTC-[A-Z]+-\d+")
SKIP_DIRS = {"node_modules", ".venv", "venv", ".git", "test-results", "playwright-report", "__pycache__"}


def files(pattern: str):
    for p in ROOT.glob(pattern):
        if p.is_file() and not SKIP_DIRS & set(p.parts):
            yield p


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def requirement_ids() -> set[str]:
    text = read(ROOT / "sqa/01-planning" / "01-requirements.md")
    return {m for line in text.splitlines() if line.startswith("| REQ-") for m in REQ_RE.findall(line.split("|")[1])}


def test_case_rows() -> dict[str, str]:
    """TC id -> first REQ id on its row (from test-cases.csv, the machine-readable copy)."""
    rows = {}
    path = ROOT / "sqa/02-manual" / "test-cases.csv"
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("id", "").startswith("TC-"):
                rows[row["id"].strip()] = row.get("requirement", "").strip()
    return rows


def md_test_case_ids() -> set[str]:
    text = read(ROOT / "sqa/02-manual" / "test-cases.md")
    return {m for line in text.splitlines() if line.startswith("| TC-") for m in TC_RE.findall(line.split("|")[1])}


def automated_refs() -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    ui = ROOT / "sqa/web-ui-playwright" / "tests"
    for p in ui.glob("*.spec.ts") if ui.exists() else []:
        for m in re.finditer(r"type:\s*'testcase',\s*description:\s*'(TC-[A-Z]+-\d+)'", read(p)):
            refs.setdefault(m.group(1), []).append(p.name)
    api = ROOT / "sqa/api-testing" / "tests"
    for p in api.glob("test_*.py") if api.exists() else []:
        for m in re.finditer(r'"""\s*(TC-[A-Z]+-\d+)[a-z]?\b', read(p)):
            refs.setdefault(m.group(1), []).append(p.name)
    return refs


def csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as fh:
        return [r for r in csv.DictReader(fh) if any((v or "").strip() for v in r.values())]


def count_placeholders() -> dict[str, int]:
    counts = {"TODO": 0, "EXAMPLE": 0, "<USERNAME>": 0}
    this = Path(__file__).resolve()
    for p in ROOT.rglob("*"):
        if (not p.is_file() or SKIP_DIRS & set(p.parts) or p.resolve() == this
                or p.suffix not in {".md", ".ts", ".py", ".csv", ".yml", ".yaml", ".json", ".html"}):
            continue
        if p.name in {"portfolio_status.py", "START-HERE.md", "PUBLISH-CHECKLIST.md"}:
            continue
        text = read(p)
        counts["TODO"] += len(re.findall(r"\bTODO\b", text))
        counts["EXAMPLE"] += len(re.findall(r"\bEXAMPLE\b", text))
        counts["<USERNAME>"] += text.count("<USERNAME>") + text.count("&lt;USERNAME&gt;")
    return counts


def bug_count() -> int:
    index = ROOT / "sqa/03-bug-reports" / "index.md"
    if not index.exists():
        return 0
    return len([ln for ln in read(index).splitlines() if re.match(r"\|\s*BUG-\d+", ln)])


def calibration(rows: list[dict]) -> str | None:
    usable = [r for r in rows if r.get("confidence_pct", "").strip().isdigit() and r.get("match", "").strip() in ("yes", "no")]
    if len(usable) < 10:
        return None
    high = [r for r in usable if int(r["confidence_pct"]) >= 80]
    out = [f"  rows with confidence+match: {len(usable)}"]
    if high:
        right = sum(r["match"] == "yes" for r in high)
        out.append(f"  stated confidence >= 80%: right {right}/{len(high)} ({right / len(high):.0%})")
    return "\n".join(out)


def main() -> int:
    strict = "--strict" in sys.argv
    errors: list[str] = []
    warnings: list[str] = []

    reqs = requirement_ids()
    tcs = test_case_rows()
    md_tcs = md_test_case_ids()
    refs = automated_refs()

    for tc, req in tcs.items():
        if req not in reqs:
            errors.append(f"{tc}: unknown requirement '{req}' in test-cases.csv")
    for tc in sorted(set(tcs) ^ md_tcs):
        errors.append(f"{tc}: present in only one of test-cases.md / test-cases.csv")
    for tc, where in refs.items():
        if tc not in tcs:
            errors.append(f"{tc}: referenced by {', '.join(where)} but not defined in test-cases.csv")
    covered = {tcs[tc] for tc in tcs if tcs[tc]}
    for req in sorted(reqs - covered):
        warnings.append(f"{req}: no test case yet")
    for tc in sorted(set(tcs) - set(refs)):
        warnings.append(f"{tc}: not automated (fine if manual-only)")

    ai_rows = csv_rows(ROOT / "sqa/ai-testing" / "ai-test-log.csv")
    conf_rows = csv_rows(ROOT / "docs" / "thinking" / "confidence-log.csv")
    placeholders = count_placeholders()

    print("Portfolio status")
    print(f"  Requirements:           {len(reqs)}")
    print(f"  Manual test cases:      {len(tcs)}")
    print(f"  Automated (referenced): {len(set(refs) & set(tcs))}")
    print(f"  Bug reports:            {bug_count()}")
    print(f"  AI-test log rows:       {len(ai_rows)}")
    print(f"  Confidence log rows:    {len(conf_rows)}")
    print(f"  Placeholders:           TODO={placeholders['TODO']} EXAMPLE={placeholders['EXAMPLE']} <USERNAME>={placeholders['<USERNAME>']}")
    cal = calibration(conf_rows)
    if cal:
        print("Confidence calibration:\n" + cal)

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print("  -", w)
    if strict and any(placeholders.values()):
        errors.append("placeholders remain (TODO/EXAMPLE/<USERNAME>) — resolve before publishing")
    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print("  -", e)
        return 1
    print("\nNo errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
