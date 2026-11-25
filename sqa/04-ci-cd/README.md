# 04 — CI/CD

Workflows live in `.github/workflows/` (GitHub requires that path).

| Workflow | Trigger | What it does |
|---|---|---|
| `ui-tests.yml` | push/PR on `sqa/web-ui-playwright/**`, nightly, manual | Job 1: typecheck + suite against the local mock. Job 2: suite on chromium/firefox/webkit against the real demo site, summary in the run page, reports as artifacts |
| `api-tests.yml` | push/PR on `sqa/api-testing/**`, nightly, manual | Ruff, mock self-test, then real practice API; JUnit + HTML artifacts |
| `portfolio-checks.yml` | every push/PR | `scripts/portfolio_status.py` (traceability, orphan ids) and AI-test precision |

## Design choices
- **Least privilege:** `permissions: contents: read`.
- **Path filters** avoid running UI tests for an API-only change.
- **Two jobs per suite:** the mock job isolates framework faults from third-party site outages, so a red real-site job with a green mock job points at the target, not at the code.
- **Retries only in CI** (config), flaky results counted separately in the summary.
- **Nightly cron** catches drift in the practice sites.
- Secrets: none required. If you add any, use GitHub Actions Secrets and never echo them.

## Checklist
- [ ] Push; open the Actions tab and confirm the three workflows are green
- [ ] Replace `<USERNAME>/<REPO>` in the README badges
- [ ] Screenshot a green run into `sqa/05-reports/latest/` (real run only)
- [ ] Note any real-site failure in `sqa/03-bug-reports/` or `docs/thinking/decision-log.md`
