"""Compute AI-test precision from ai-test-log.csv (stdlib only).

precision = accepted / generated   (fixed rows count as accepted only if verdict == accepted)
Usage: python sqa/ai-testing/precision.py
"""
import csv
import sys
from collections import Counter
from pathlib import Path

LOG = Path(__file__).with_name("ai-test-log.csv")


def load(path: Path = LOG) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return [row for row in csv.DictReader(fh) if any(v.strip() for v in row.values() if v)]


def summarize(rows: list[dict]) -> dict:
    verdicts = Counter(r["verdict"].strip().lower() for r in rows)
    generated = len(rows)
    accepted = verdicts["accepted"]
    categories = Counter(
        r["failure_category"].strip() for r in rows
        if r["verdict"].strip().lower() in ("rejected", "fixed") and r["failure_category"].strip()
    )

    def minutes(col: str) -> float:
        return sum(float(r[col]) for r in rows if r[col].strip())

    return {
        "generated": generated,
        "accepted": accepted,
        "fixed": verdicts["fixed"],
        "rejected": verdicts["rejected"],
        "precision": (accepted / generated) if generated else None,
        "categories": dict(categories),
        "minutes_ai": minutes("minutes_ai"),
        "minutes_manual_est": minutes("minutes_manual_est"),
    }


def main() -> int:
    rows = load()
    s = summarize(rows)
    if not s["generated"]:
        print("AI-test log is empty: no precision to report (this is fine until you run the experiment).")
        return 0
    print(f"Generated: {s['generated']}  Accepted: {s['accepted']}  Fixed: {s['fixed']}  Rejected: {s['rejected']}")
    print(f"Precision (accepted / generated): {s['precision']:.0%}")
    if s["generated"] < 20:
        print("Note: fewer than 20 rows; treat the percentage as anecdotal.")
    if s["categories"]:
        print("Failure categories:", ", ".join(f"{k}={v}" for k, v in s["categories"].items()))
    print(f"Time: AI {s['minutes_ai']:.0f} min vs manual estimate {s['minutes_manual_est']:.0f} min (estimates are yours, not measured)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
