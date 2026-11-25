# 05 — Reports

| File | Purpose |
|---|---|
| `generate_summary.py` | Turns Playwright `results.json` and pytest `junit.xml` into a Markdown table |
| `test-summary-report.md` | The human-written report for a test cycle |
| `latest/` | Evidence from the most recent real run (git-tracked placeholders only) |

```bash
python sqa/05-reports/generate_summary.py \
  --playwright sqa/web-ui-playwright/test-results/results.json \
  --junit sqa/api-testing/reports/junit.xml --out sqa/05-reports/latest/summary.md
```
Pass rate = (passed + flaky) / (total − skipped). In CI the same script writes to the run summary.
