# 03 — Risk Assessment

Risk score = **Likelihood (1–5) × Impact (1–5)**. Focus testing effort on the highest scores. Re-score after every release or escaped S1/S2 bug.

## Product risks (what could go wrong in the SUT)
| ID | Risk | Area | L | I | Score | Mitigation / test focus |
|---|---|---|---|---|---|---|
| R-01 | EXAMPLE: Users can access protected pages without logging in | Auth | 3 | 5 | 15 | Direct-URL access tests, session tests |
| R-02 | EXAMPLE: Cart total/price calculated incorrectly | Checkout | 3 | 5 | 15 | Boundary & calculation cases, E2E |
| R-03 | EXAMPLE: Form validation missing → bad data accepted | Checkout | 4 | 3 | 12 | Negative and boundary cases |
| R-04 | EXAMPLE: Layout breaks on mobile | UI | 3 | 3 | 9 | Mobile viewport project |
| R-05 | EXAMPLE: API returns inconsistent status codes/errors | API | 4 | 3 | 12 | Contract and negative tests |
| TODO | | | | | | |

## Project risks (what could go wrong with testing)
| ID | Risk | L | I | Score | Mitigation |
|---|---|---|---|---|---|
| P-01 | Practice site unavailable or changed | 3 | 4 | 12 | Env-driven URLs; document tested date; local mocks |
| P-02 | Flaky automation due to shared/public environment | 3 | 3 | 9 | Retries in CI only; independent tests; no fixed sleeps |
| P-03 | Scope creep / unfinished portfolio | 4 | 4 | 16 | P0 tier first; weekly review |
| P-04 | Testing outside permitted scope | 2 | 5 | 10 | Follow [`SECURITY.md`](../../SECURITY.md) |
| P-05 | AI-generated tests give false confidence (weak assertions, invented selectors) | 4 | 4 | 16 | Verification gate; mutation check; measured precision |

## Risk → test mapping
Update after writing test cases.

| Risk | Test cases |
|---|---|
| R-01 | TODO |
| R-02 | TODO |
