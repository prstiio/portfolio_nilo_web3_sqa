#!/usr/bin/env python3
"""Turn Playwright JSON and/or pytest JUnit results into a Markdown summary (stdlib only).

pass rate = (passed + flaky) / (total - skipped)

Usage:
  python sqa/05-reports/generate_summary.py --playwright sqa/web-ui-playwright/test-results/results.json \
      --junit sqa/api-testing/reports/junit.xml --out sqa/05-reports/latest/summary.md
"""
import argparse
import json
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def playwright_counts(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    counts = {"passed": 0, "failed": 0, "flaky": 0, "skipped": 0}
    duration_ms = float(data.get("stats", {}).get("duration", 0))

    def walk(suite: dict) -> None:
        for spec in suite.get("specs", []):
            for test in spec.get("tests", []):
                status = test.get("status")  # expected | unexpected | flaky | skipped
                key = {"expected": "passed", "unexpected": "failed", "flaky": "flaky", "skipped": "skipped"}.get(status)
                if key:
                    counts[key] += 1
        for child in suite.get("suites", []):
            walk(child)

    for suite in data.get("suites", []):
        walk(suite)
    counts["duration_s"] = duration_ms / 1000
    return counts


def junit_counts(path: Path) -> dict:
    root = ET.parse(path).getroot()
    suites = [root] if root.tag == "testsuite" else list(root.iter("testsuite"))
    total = sum(int(s.get("tests", 0)) for s in suites)
    failed = sum(int(s.get("failures", 0)) + int(s.get("errors", 0)) for s in suites)
    skipped = sum(int(s.get("skipped", 0)) for s in suites)
    duration = sum(float(s.get("time", 0)) for s in suites)
    return {"passed": total - failed - skipped, "failed": failed, "flaky": 0, "skipped": skipped, "duration_s": duration}


def pass_rate(c: dict) -> str:
    denominator = c["passed"] + c["failed"] + c["flaky"]
    return f"{(c['passed'] + c['flaky']) / denominator:.1%}" if denominator else "n/a"


def row(name: str, c: dict) -> str:
    total = c["passed"] + c["failed"] + c["flaky"] + c["skipped"]
    return f"| {name} | {total} | {c['passed']} | {c['failed']} | {c['flaky']} | {c['skipped']} | {pass_rate(c)} | {c['duration_s']:.1f}s |"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--playwright", type=Path)
    ap.add_argument("--junit", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    rows = []
    if args.playwright and args.playwright.exists():
        rows.append(row("UI (Playwright)", playwright_counts(args.playwright)))
    if args.junit and args.junit.exists():
        rows.append(row("API (pytest)", junit_counts(args.junit)))
    if not rows:
        print("No result files found; nothing to summarize.", file=sys.stderr)
        return 1

    md = "## Test summary\n\n| Suite | Total | Passed | Failed | Flaky | Skipped | Pass rate | Duration |\n|---|---|---|---|---|---|---|---|\n"
    md += "\n".join(rows) + "\n\nPass rate = (passed + flaky) / (total − skipped).\n"
    if args.out:
        # GITHUB_STEP_SUMMARY must be appended to; a normal file is overwritten.
        mode = "a" if os.environ.get("GITHUB_STEP_SUMMARY") == str(args.out) else "w"
        with args.out.open(mode, encoding="utf-8") as fh:
            fh.write(md)
    else:
        print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
