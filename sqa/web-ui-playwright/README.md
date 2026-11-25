# UI automation — Playwright + TypeScript

Target: [SauceDemo](https://www.saucedemo.com), a public shop built for test practice (see [SECURITY.md](../../SECURITY.md)).

## Run
```bash
npm install            # commit package-lock.json afterwards
npx playwright install
cp .env.example .env
npm test               # all projects (chromium, firefox, webkit, mobile-chrome)
npm run test:smoke     # @smoke only
npm run test:regression
npm run report         # open the HTML report
npm run typecheck
```

## Offline / framework self-test
```bash
npm run test:mock      # same specs against mock-sut/ (starts its own server on :4173)
```
`mock-sut/` is a local test double modelled on the demo shop. A green mock run proves the framework logic. It is **not** evidence about the real site.

## Layout and conventions
| Path | Role |
|---|---|
| `pages/` | Page objects: locators + actions, no assertions (except tiny `expect*` helpers) |
| `fixtures/index.ts` | Injects page objects; `loggedInInventory` logs in once per test |
| `tests/` | Specs by feature, tagged `@smoke` / `@regression` |
| `utils/` | Synthetic test data and helpers |

- Every test carries `annotation: { type: 'testcase', description: 'TC-…' }`; `scripts/portfolio_status.py` checks the id exists.
- Locators: role → label → text → test id (`data-test`). No `waitForTimeout`; web-first assertions only.
- Flaky check before accepting a new test: `npm run gate` (chromium, 5 repeats).

## Mutation check (does the test really fail?)
Break the behavior in `mock-sut/index.html` (e.g. reverse the `lohi` sort), run that test, confirm it goes red, revert. Done once during the v2 build for the sort test; see `sqa/ai-testing/verification-gate.md`.

Status: 12 tests green on the local mock (3 repeats each). Not yet run against the real site from the build environment.
