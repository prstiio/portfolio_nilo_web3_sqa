# AGENTS.md — Rules for AI assistants working on this repository

This is a **QA portfolio**. Its value is credibility. Follow these rules strictly.

## 1. Integrity (highest priority)
- **Never fabricate** test results, bug reports, metrics, screenshots, pass rates, or "findings". If something was not actually executed or observed, do not write it as if it was.
- Mark unfinished content with `TODO`. Mark illustrative content with `EXAMPLE`. Never remove these markers unless the owner has verified the content.
- Test cases may be drafted by AI, but the owner must execute them manually before the status changes from `Not Run`.
- Bugs must come from real observation of the SUT. Do not invent defects.
- Every number in `README.md` or a report must be reproducible: from a command (`python scripts/portfolio_status.py`), a CI run, or a file. See `docs/thinking/evidence-register.md`.

## 2. Scope & safety
- Only test targets listed in `docs/PRD.md` → *In scope*. Read [SECURITY.md](SECURITY.md) first.
- Do not generate load, fuzzing, scanning, or exploit code aimed at third-party production systems.
- Never commit secrets, tokens, real personal data, or credentials. Use `.env` (git-ignored) and `.env.example`.

## 3. Workflow (PLAN → SPECIFY → BUILD → TEST)
1. **PLAN** — update `docs/PRD.md`, `sqa/01-planning/*` before writing tests.
2. **SPECIFY** — write/adjust test cases in `sqa/02-manual/` and keep traceability in `sqa/01-planning/04-traceability-matrix.md`.
3. **BUILD** — implement automation only for cases that exist in the specification.
4. **TEST** — run, report bugs in `sqa/03-bug-reports/`, summarize in `sqa/05-reports/`.

## 4. ID conventions
| Type | Format | Example |
|---|---|---|
| Requirement | `REQ-<AREA>-<NN>` / `NFR-<AREA>-<NN>` | `REQ-LOGIN-01` |
| Test case | `TC-<AREA>-<NNN>` | `TC-LOGIN-001` |
| Bug | `BUG-<NNN>` | `BUG-001` |
| Exploratory session | `ES-<NNN>` | `ES-001` |

Traceability convention (checked by `scripts/portfolio_status.py`):
- **Playwright:** `annotation: { type: 'testcase', description: 'TC-…' }` on the test.
- **pytest:** the TC id at the start of the test's docstring (`"""TC-API-006: …"""`). A suffix letter (`TC-API-007a`) is allowed and maps to `TC-API-007`.
- Do **not** invent custom pytest markers: `pytest.ini` uses `--strict-markers`, so an unregistered marker fails the run.

## 5. Decision rights: what AI may and may not do here
Details and rationale: [`sqa/ai-testing/delegation-rules.md`](sqa/ai-testing/delegation-rules.md).

| AI may draft (owner verifies) | Owner decides (AI must not) |
|---|---|
| Candidate test cases, input variations, boundary values | Scope, strategy, exit criteria, risk acceptance |
| Candidate UI/API tests | What the correct result is (the test oracle) |
| Bug-report drafts from the owner's own notes | Whether a bug is real, and its severity |
| Log/report summaries | Release recommendation; any security/financial sign-off |

Every AI-generated test must pass the gate in [`sqa/ai-testing/verification-gate.md`](sqa/ai-testing/verification-gate.md) and be logged in `sqa/ai-testing/ai-test-log.csv` before it counts as portfolio evidence.

## 5b. Site pages (`index.html`, `web3/`, `sqa/index.html`, `projects/`)
- Every claim on a page needs linked evidence (demo, code path, screenshot, report). Without it, mark `TODO` or `EXAMPLE`.
- Never state that something is on-chain, deployed, or production-ready unless a link proves it. Web3 work is testnet or local only.
- Keep HTML static and dependency-free; shared styles live in `assets/style.css`; check at 390 px width (no horizontal page scroll).
- The same project may appear on both pages; describe the contribution and the evidence differently for each role, and never copy results that were not observed.
- Pages are in English (international audience).

## 6. Tools allowed
- UI: Playwright + TypeScript (Page Object Model, fixtures). No `waitForTimeout` / fixed sleeps; use auto-waiting and web-first assertions.
- API: pytest + requests + jsonschema.
- CI: GitHub Actions.
- Do not add new frameworks/dependencies without noting the reason in `docs/ARCHITECTURE.md`.

## 7. Code & docs style
- Follow [docs/CODE-STYLE.md](docs/CODE-STYLE.md) and [docs/DESIGN-SYSTEM.md](docs/DESIGN-SYSTEM.md).
- Keep tests independent and deterministic; one behavior per test; clear names.
- Page objects contain locators and actions; **assertions live in tests** (small `expect*` helpers are acceptable).
- Docs are written in English (portfolio audience is international). Keep them concise.

## 8. Before finishing any task
- [ ] Tests run locally (or state clearly that they were not run, and against which target)
- [ ] `python scripts/portfolio_status.py` shows no errors (orphan test references, unknown IDs)
- [ ] No secrets, no fabricated data
- [ ] README/docs updated if structure changed
