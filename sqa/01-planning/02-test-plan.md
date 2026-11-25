# 02 — Test Plan

| Field | Value |
|---|---|
| Project | TODO |
| Version | 0.1 |
| Author | TODO |
| Date | TODO |

## 1. Introduction
TODO — purpose of this plan and the SUT in one paragraph. See [`00-product-summary.md`](00-product-summary.md).

## 2. Scope
**In scope:** TODO (features/requirements from [`01-requirements.md`](01-requirements.md))
**Out of scope:** TODO (e.g. performance, security testing, third-party payment)

## 3. Test approach
Follows [`docs/SQA-STRATEGY.md`](../../docs/SQA-STRATEGY.md).

| Type | Approach | Tooling | Owner |
|---|---|---|---|
| Functional (manual) | Test cases from requirements, BVA/EP | Markdown/CSV | TODO |
| Exploratory | Time-boxed charters | Session notes | TODO |
| UI automation | Smoke + critical flows | Playwright | TODO |
| API automation | CRUD, auth, negative, schema | pytest | TODO |
| Cross-browser | Chromium / Firefox / WebKit / mobile emulation | Playwright projects | TODO |
| Non-functional (basic) | Accessibility, performance, security-awareness checklist | Manual | TODO |
| AI-assisted | Candidate tests through the verification gate | LLM + `sqa/ai-testing/` | TODO |

## 4. Test items & features
| Feature | Requirements | Risk score (see `03-risk-assessment.md`) | Depth |
|---|---|---|---|
| TODO | REQ-... | TODO | manual + automation / smoke only |

## 5. Environment & tools
| Item | Detail |
|---|---|
| SUT URL(s) | TODO |
| Browsers | Chromium, Firefox, WebKit |
| Runtime | Node 20+, Python 3.11+ |
| CI | GitHub Actions |
| Defect tracking | `sqa/03-bug-reports/` |

## 6. Entry / exit criteria
**Entry:** requirements reviewed, environment reachable, test data ready.
**Exit:** all planned cases executed, no open S1/S2 without decision, CI green, summary report issued.

## 7. Schedule
| Activity | Start | End |
|---|---|---|
| Planning | TODO | TODO |
| Test design | TODO | TODO |
| Manual execution | TODO | TODO |
| Automation | TODO | TODO |
| Reporting | TODO | TODO |

## 8. Deliverables
Test plan · test cases · execution log · bug reports · automation code · CI pipeline · test summary report · AI experiment report.

## 9. Risks & assumptions
See [`03-risk-assessment.md`](03-risk-assessment.md).

## 10. Approval
TODO (self-review checklist or reviewer name/date).
