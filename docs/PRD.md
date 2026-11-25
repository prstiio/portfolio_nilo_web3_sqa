# Product Requirements Document (PRD) — Personal Portfolio (Web3 Builder + SQA Engineer)

> PLAN phase. Defines what this portfolio must achieve. Fill every `TODO`.

## 1. Problem
Hiring managers and clients cannot judge a QA engineer from a CV alone. They need evidence of **how** the candidate analyzes, designs, automates, reports on quality, and uses AI without trusting it blindly.

## 2. Goal
One personal repository with two focused entry points: a **Web3 Builder** page (what I build) and an **SQA Engineer** page (how I verify quality), plus one shared case study (NILO). Decision: one repo, not two, because both portfolios describe the same work and would otherwise need syncing. Revisit only if audience, identity, or maintenance diverge.

SQA goal in detail: Provide a public, reproducible portfolio that demonstrates the full QA lifecycle on one system under test (SUT), end to end, and that shows measured (not claimed) results.

## 3. Business objective (strategic link)
| Item | Value |
|---|---|
| Owner's objective | TODO (e.g. land first paid QA/crowdtesting work within N weeks; build a Web3 QA specialization) |
| How this portfolio serves it | TODO (e.g. proof of work for platform profiles and proposals) |
| Decision log | [`thinking/decision-log.md`](thinking/decision-log.md) records why the SUT and niche were chosen |

## 4. Target audience
| Audience | What they look for |
|---|---|
| Recruiters / hiring managers | Structure, clarity, consistency, evidence of real work |
| Freelance clients | Ability to deliver a test strategy + working automation + reports |
| Crowdtesting platforms | Bug-report quality and exploratory thinking |

## 5. System under test (SUT)
| Layer | Target | Why | Environment |
|---|---|---|---|
| UI | TODO (default: SauceDemo — https://www.saucedemo.com) | Practice site; common benchmark | Public |
| API | TODO (default: Restful-Booker — https://restful-booker.herokuapp.com) | Practice API with auth + CRUD | Public |
| Local fallback | Bundled mocks (`sqa/web-ui-playwright/mock-sut`, `sqa/api-testing/tools/mock_booker.py`) | Offline runs; proves framework logic. **Not** evidence about the real sites | Local |
| Differentiator | TODO (e.g. open-source smart contract, local dApp, AI app) | Rare skill; stands out | Local / testnet |

## 6. In scope
- Functional testing (UI + API), negative/boundary cases
- Exploratory testing sessions
- Cross-browser and basic responsive checks
- Basic accessibility checks (keyboard, labels, contrast)
- Test automation (Playwright, pytest) and CI
- AI-assisted testing with a documented verification gate and measured precision
- Defect reporting and test summary reporting
- Static portfolio site (landing, Web3, SQA, NILO case study) with claims backed by linked evidence

## 7. Out of scope
- Load/stress/security testing on third-party systems (see [SECURITY.md](../SECURITY.md))
- Any target not listed in section 5
- Production data of any real person

## 8. Success criteria (measurable)
Tiers: **P0** = minimum viable portfolio (about 4 weeks). **P1** = full portfolio. **P2** = differentiators.

| # | Criterion | Target | Tier | Actual (from `scripts/portfolio_status.py`) |
|---|---|---|---|---|
| 1 | Requirements documented with IDs | ≥ 15 | P0 | TODO |
| 2 | Manual test cases | P0: 20 · P1: 40–80 | P0/P1 | TODO |
| 3 | Real bug reports (quality over quantity) | P0: ≥ 3 · P1: ≥ 10 | P0/P1 | TODO |
| 4 | Automated UI tests (Playwright) | P0: 8 · P1: 15–25 | P0/P1 | TODO |
| 5 | Automated API tests (pytest) | P0: 8 · P1: ≥ 15 | P0/P1 | TODO |
| 6 | CI pipeline green on `main` | Yes | P0 | TODO |
| 7 | Test summary report from real data | 1 | P0 | TODO |
| 8 | Traceability: every requirement ↔ ≥ 1 test case | 100% | P1 | TODO |
| 9 | AI experiment: precision measured on ≥ 20 AI-generated tests | 1 report | P1 | TODO |
| 10 | Demo video | 3–5 min | P1 | TODO |
| 11 | Differentiator repo (Web3 / AI app testing) | 1 | P2 | TODO |

## 9. Deliverables → locations
| Deliverable | Location |
|---|---|
| Product summary, requirements, test plan, risks, traceability | `sqa/01-planning/` |
| Test cases, execution log, exploratory sessions, non-functional checklist | `sqa/02-manual/` |
| Bug reports | `sqa/03-bug-reports/` |
| UI automation | `sqa/web-ui-playwright/` |
| API automation | `sqa/api-testing/` |
| AI-assisted testing evidence | `sqa/ai-testing/` |
| CI/CD | `.github/workflows/`, `sqa/04-ci-cd/` |
| Reports | `sqa/05-reports/` |
| Thinking logs (decisions, confidence, weekly review, evidence) | `docs/thinking/` |
| Landing page and shared styles | `index.html`, `assets/style.css` |
| Web3 Builder page and claim checklist | `web3/` |
| SQA Engineer page | `sqa/index.html` |
| Shared case study (NILO) | `projects/nilo.html` |

## 10. Risks
| Risk | Mitigation |
|---|---|
| Practice sites change or go offline | Env-driven URLs; document tested date; local mocks as fallback |
| Over-documenting before any test runs | P0 tier first; run the first test on day 1 |
| Portfolio looks generic | Add one differentiator; write real findings |
| Legal/ethical issues testing third-party apps | Follow [SECURITY.md](../SECURITY.md) strictly |
| Over-trusting AI output | Verification gate + measured precision |
| Stale repo | Commit at least weekly; weekly review |

## 11. Milestones
| Milestone | Tier | Target |
|---|---|---|
| M0 — Setup; first test runs | P0 | Day 1 |
| M1 — PLAN docs + 20 test cases | P0 | Week 1–2 |
| M2 — 8 UI + 8 API tests; CI green | P0 | Week 3–4 |
| M3 — Full manual + bugs + 15–25 UI + ≥ 15 API | P1 | Week 5–9 |
| M4 — AI experiment + reports + demo | P1 | Week 10–12 |
| M5 — Differentiator + publish | P2 | Week 13–16 |
