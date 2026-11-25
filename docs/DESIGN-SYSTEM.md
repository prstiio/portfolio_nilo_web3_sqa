# Design System — Test Design Standards

> In an app project, a design system keeps generated UI consistent. In a QA project the equivalent is a **test design system**: shared conventions so every artifact (human- or AI-made) looks and behaves the same. It covers the "frontend" (UI tests, reports) and the "backend" (API tests, schemas).

## Site pages
Layout: header with brand and three links; hero; cards or tables; footer. Colors are tokens in `assets/style.css` (Web3 = amber, SQA = teal), with a dark-mode override. Status badges: `EXAMPLE` or `Unverified` until evidence is linked. One H1 per page. Links to evidence use GitHub URLs with `<USERNAME>/<REPO>` filled in at publish time.

## 1. Naming
| Thing | Rule | Example |
|---|---|---|
| Requirement / test case / bug / session | IDs from `AGENTS.md` | `REQ-CHK-02`, `TC-CHK-002` |
| Playwright test title | `<subject> should <observable result>` | `empty username should show a "username required" error` |
| pytest test name | `test_<what>_<condition>_<expected>` | `test_update_without_authorization_is_rejected` |
| Spec / test files | `<feature>.spec.ts`, `test_<resource>.py` | `cart-checkout.spec.ts` |
| Branches | `test/<feature>`, `docs/<topic>`, `ci/<change>` | `test/checkout-negative` |

## 2. Tags and markers
| Tag | Meaning | Where |
|---|---|---|
| `@smoke` | Fast, critical: is the app alive and the main path usable | Playwright `tag` |
| `@regression` | Broader functional checks | Playwright `tag` |
| `smoke`, `regression`, `negative`, `schema` | pytest markers (registered in `pytest.ini`) | pytest |

## 3. UI test design (frontend)
- Locator priority: `getByRole` → `getByLabel` → `getByText` → `getByTestId` (the SUT's `data-test` attribute). Avoid CSS/XPath chains and positional selectors.
- Page objects hold locators and user-intent actions; assertions on business rules live in tests.
- Prefer fixtures over `beforeEach` chains for repeated setup (e.g. logged-in state).
- Use `test.step()` for flows longer than three actions so reports read like a story.
- Never use fixed sleeps. Wait on a condition through a web-first assertion.

## 4. API test design (backend)
- Assert three things: status code, response shape (JSON schema), key field values.
- One schema per resource in `sqa/api-testing/utils/schemas.py`; payload builders in `utils/data.py`.
- Tests create their own data through fixtures and clean up after themselves.
- Negative cases check the specific 4xx code **and** that no state changed.
- When behavior differs from documentation, decide: wrong test or real finding? Never edit an assertion just to turn it green.

## 5. Test data
Synthetic only. Defaults live in `utils/testData.ts` and `utils/data.py`. Public-demo credentials come from `.env.example`.

## 6. Document and report templates
| Template | Location |
|---|---|
| Test case | `sqa/02-manual/test-cases.md` (template block) |
| Exploratory session | `sqa/02-manual/exploratory-sessions/_TEMPLATE.md` |
| Bug report | `sqa/03-bug-reports/_TEMPLATE.md` |
| Test summary report | `sqa/05-reports/test-summary-report.md` |
| AI experiment report | `sqa/ai-testing/experiment-report.md` |
| Weekly review | `docs/thinking/weekly-review.md` |

## 7. Report visual conventions
- Status words, not colors alone: `Pass`, `Fail`, `Blocked`, `Not Run`, `Flaky`.
- Tables for comparisons; one H1 per file; relative links only.
- Numbers always carry their source (command, run link, file).
- Markers: `TODO` = unfinished, `EXAMPLE` = illustrative. Both must be gone before publishing (`scripts/portfolio_status.py --strict`).

## 8. Severity and priority vocabulary
Defined once in [`SQA-STRATEGY.md`](SQA-STRATEGY.md#5-severity--priority); do not redefine elsewhere.
