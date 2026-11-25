# Prstio: Web3 Builder and SQA Engineer

> One personal portfolio, two entry points. Same projects, different lenses: **what I build** (Web3) and **how I check its quality** (SQA).

[![UI Tests](https://github.com/<USERNAME>/<REPO>/actions/workflows/ui-tests.yml/badge.svg)](https://github.com/<USERNAME>/<REPO>/actions/workflows/ui-tests.yml)
[![API Tests](https://github.com/<USERNAME>/<REPO>/actions/workflows/api-tests.yml/badge.svg)](https://github.com/<USERNAME>/<REPO>/actions/workflows/api-tests.yml)
[![Portfolio checks](https://github.com/<USERNAME>/<REPO>/actions/workflows/portfolio-checks.yml/badge.svg)](https://github.com/<USERNAME>/<REPO>/actions/workflows/portfolio-checks.yml)

**Author:** TODO name · **Contact:** TODO email / LinkedIn · **Live site:** TODO (`https://<USERNAME>.github.io/`)

## Why one repo, not two
Web3 and SQA are two views of the same work (for example NILO). One repo means one source of truth, no content to sync, and a clear story: build it, then prove it works. Split into two repos only if the audiences, identity, or maintenance diverge for real.

## Entry points
| Page | Audience | Files |
|---|---|---|
| Landing | Anyone: picks a focus | [`index.html`](index.html) |
| Web3 Builder | Web3 clients and teams | [`web3/`](web3) |
| SQA Engineer | QA clients and employers | [`sqa/`](sqa) |
| NILO case study | Both | [`projects/nilo.html`](projects/nilo.html) |

## Structure
```
portfolio/
├── index.html            landing page (pick a focus)
├── assets/style.css      shared styles (light/dark, mobile-first)
├── web3/                 Web3 Builder portfolio (page + README)
├── sqa/                  SQA Engineer portfolio
│   ├── 01-planning/      requirements, test plan, risks, traceability
│   ├── 02-manual/        test cases, execution log, exploratory sessions
│   ├── 03-bug-reports/   template, index, evidence
│   ├── web-ui-playwright/  UI automation (+ local mock)
│   ├── api-testing/      API automation (+ local mock)
│   ├── ai-testing/       delegation rules, 5-step gate, AI-test log, precision
│   ├── 04-ci-cd/         pipeline documentation
│   ├── 05-reports/       summary generator + test summary report
│   └── web3-testing/     Web3 QA templates
├── projects/nilo.html    shared case study
├── docs/                 PRD, Design System, Architecture, SQA, Code Style, thinking logs
├── scripts/              portfolio_status.py (traceability and placeholder checks)
├── AGENTS.md  SECURITY.md  START-HERE.md  PUBLISH-CHECKLIST.md
└── .github/workflows/    CI (ui, api, portfolio checks)
```

## Documents (PLAN → SPECIFY → BUILD → TEST)
| Document | File |
|---|---|
| PRD | [`docs/PRD.md`](docs/PRD.md) |
| Design System | [`docs/DESIGN-SYSTEM.md`](docs/DESIGN-SYSTEM.md) |
| Architecture | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Agents (AI rules) | [`AGENTS.md`](AGENTS.md) |
| Security | [`SECURITY.md`](SECURITY.md) |
| Confidentiality workflow | [`docs/CONFIDENTIALITY-WORKFLOW.md`](docs/CONFIDENTIALITY-WORKFLOW.md) |
| Code Style | [`docs/CODE-STYLE.md`](docs/CODE-STYLE.md) |
| SQA | [`docs/SQA-STRATEGY.md`](docs/SQA-STRATEGY.md) |
| Thinking logs | [`docs/thinking/`](docs/thinking) |
Full mapping: [`docs/DOC-MAP.md`](docs/DOC-MAP.md).

## Run
```bash
# UI tests (from the repo root)
cd sqa/web-ui-playwright && npm install && npx playwright install && cp .env.example .env
npm test              # real demo site
npm run test:mock     # offline self-test against the local mock

# API tests
cd sqa/api-testing && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env && pytest

# Repo health (from the repo root)
python scripts/portfolio_status.py
```

## Publish as a website
GitHub → Settings → Pages → Deploy from branch `main`, folder `/ (root)`. Name the repo `<USERNAME>.github.io` for `https://<USERNAME>.github.io/`. A `.nojekyll` file is included so files are served as they are.

## Results
Paste numbers from `python scripts/portfolio_status.py` after real runs. TODO.
