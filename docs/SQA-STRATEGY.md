# SQA Strategy

> SPECIFY phase. The rules that make testing consistent. Adjust to your SUT.

## 1. Quality objectives
- Detect functional defects before release
- Keep a fast, reliable regression suite
- Make results traceable, repeatable, and visible
- Use AI to speed up test creation **without** lowering the evidence standard

## 2. Test levels & types
| Level / Type | Applied to | Tool | Folder |
|---|---|---|---|
| Static review (requirements) | Requirements | Manual | `sqa/01-planning/` |
| Functional (manual) | UI flows | Manual | `sqa/02-manual/` |
| Exploratory | Whole app | Session charters | `sqa/02-manual/exploratory-sessions/` |
| UI end-to-end | Critical journeys | Playwright | `sqa/web-ui-playwright/` |
| API / contract | Endpoints | pytest + jsonschema | `sqa/api-testing/` |
| Cross-browser / responsive | UI | Playwright projects | `sqa/web-ui-playwright/` |
| Accessibility, performance, security basics | UI/API | Manual checklist | `sqa/02-manual/non-functional-checklist.md` |
| Regression | Smoke + core flows | CI | `.github/workflows/` |
| AI-assisted test generation | Candidate tests | LLM + gate | `sqa/ai-testing/` |

## 3. Test design techniques used
Equivalence partitioning · Boundary value analysis · Decision tables · State transition · Error guessing · Exploratory charters.

## 4. Priority of what to automate
1. Smoke (is the app alive; can a user log in) → `@smoke`
2. Critical business flows (e.g. checkout) → `@regression`
3. Stable, repetitive validations (forms, sorting)
4. Do **not** automate: one-off checks, volatile UI, visual judgments, cases whose oracle needs human judgment.

Risk drives depth: score each feature `Likelihood (1–5) × Impact (1–5)` in [`sqa/01-planning/03-risk-assessment.md`](../sqa/01-planning/03-risk-assessment.md) and spend effort in that order.

## 5. Severity & priority
| Severity | Definition | Example |
|---|---|---|
| S1 Critical | System unusable / data loss / security issue; no workaround | Cannot log in at all |
| S2 Major | Core feature broken; workaround exists | Checkout total wrong |
| S3 Minor | Non-core feature or cosmetic with limited impact | Sort order inconsistent on edge case |
| S4 Trivial | Cosmetic / typo | Misaligned icon |

| Priority | Meaning |
|---|---|
| P1 | Fix immediately / blocks release |
| P2 | Fix in current cycle |
| P3 | Fix when convenient |
| P4 | Backlog |

Severity = impact on the product. Priority = urgency to fix. They can differ.

## 6. Defect lifecycle
`New → Triaged → In Progress → Fixed → Verified → Closed` (or `Rejected` / `Duplicate` / `Won't Fix`). Status is tracked in `sqa/03-bug-reports/index.md`.

## 7. Entry & exit criteria
**Entry:** requirements reviewed · environment reachable · test data ready · test cases drafted.
**Exit:** 100% planned cases executed · no open S1/S2 without a documented decision · automation suite green in CI · summary report produced · `scripts/portfolio_status.py` reports no errors.

## 8. AI-assisted testing policy
- AI proposes; the owner verifies and decides. Delegation boundaries: [`sqa/ai-testing/delegation-rules.md`](../sqa/ai-testing/delegation-rules.md).
- Every AI-generated test passes the 5-step gate ([`sqa/ai-testing/verification-gate.md`](../sqa/ai-testing/verification-gate.md)) and is logged; precision is computed from the log, never estimated.
- Delegate only when a result is cheap to verify by machine, reversible, and low-impact. Keep strategy, oracles, severity, and security/financial sign-off with the owner.

## 9. Test environment
| Item | Value |
|---|---|
| Browsers | Chromium, Firefox, WebKit (+ mobile Chrome emulation) |
| OS (local) | TODO |
| Node / Python | Node 20+, Python 3.11+ |
| SUT version/date tested | TODO |

## 10. Test data
Synthetic only. Each automated test creates and cleans up its own data when possible.

## 11. Metrics reported
Total tests · pass / fail / flaky / skipped · pass rate · duration · defects by severity · requirement coverage · automation coverage · AI-test precision (accepted ÷ generated).

```latex
\text{pass rate} = \frac{\text{passed} + \text{flaky}}{\text{total} - \text{skipped}} \times 100\%
```

## 12. Flaky test policy
A test that fails intermittently is quarantined (`test.fixme` / `xfail` with a linked issue), root-caused within the cycle, and never "fixed" with fixed sleeps. Retries run only in CI, and flaky results are counted separately.

## 13. Naming conventions
See [`DESIGN-SYSTEM.md`](DESIGN-SYSTEM.md#1-naming).
