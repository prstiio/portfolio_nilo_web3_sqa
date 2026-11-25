# Verification gate (5 steps)

An AI-generated test is **not portfolio evidence** until it passes all five steps. Record the outcome of each step in `ai-test-log.csv`.

| # | Step | How | Log column |
|---|---|---|---|
| 1 | **Builds** | `cd sqa/web-ui-playwright && npm run typecheck` / `cd sqa/api-testing && ruff check .` | `build_ok` |
| 2 | **Stable** | UI: `cd sqa/web-ui-playwright && npm run gate`. API: run the single test 5 times (`for i in 1 2 3 4 5; do pytest -q tests/<file>.py::<test> || break; done`) | `repeat5_ok` |
| 3 | **Adds value** | Covers a requirement/case or behavior not already covered (check `sqa/01-planning/04-traceability-matrix.md`) | `adds_value` |
| 4 | **Can fail** | Mutation check (below): break the SUT behavior on purpose and confirm the test goes red | `mutation_killed` |
| 5 | **Assertions read** | You read every assertion and can explain what it proves; no `toBeTruthy()` on a locator, no assertion-free tests | `assertion_reviewed` |

## Mutation check (step 4)
1. UI against the local mock: edit `sqa/web-ui-playwright/mock-sut/index.html` to break the behavior under test (e.g. make the sort ascending only, drop the badge update).
2. API: edit `sqa/api-testing/tools/mock_booker.py` (e.g. return 200 instead of 403 when no token).
3. Run only that test. It must **fail**. Then revert the edit (`git checkout -- <file>`).
4. If it still passes, the test is decoration: reject it or strengthen the assertion.

## Verdicts
- `accepted`: all five steps passed.
- `rejected`: a step failed and the test was dropped.
- `fixed`: failed a step, owner repaired it, then it passed (counts as accepted for precision only if the fix was small; note effort in `minutes_manual_est`).

Use `failure_category` for rejected/fixed rows: `bad-locator`, `weak-assertion`, `wrong-oracle`, `flaky`, `duplicate`, `hallucinated-api`, `other`.
