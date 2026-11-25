# Document Map — AI-project documents applied to the portfolio (Web3 + SQA)

The usual set of documents that keeps AI-assisted work consistent, mapped to where each lives in this repository. Workflow: **PLAN → SPECIFY → BUILD → TEST**.

| # | Standard document | In this repo | Phase | What it controls |
|---|---|---|---|---|
| 1 | Product Requirements Document (PRD) | [`PRD.md`](PRD.md) + `sqa/01-planning/` | PLAN | Why the portfolio exists, scope, measurable success criteria |
| 2 | Design System | [`DESIGN-SYSTEM.md`](DESIGN-SYSTEM.md) | SPECIFY | Naming, tags, locator and API-test standards, templates, report conventions |
| 3 | Architecture | [`ARCHITECTURE.md`](ARCHITECTURE.md) | SPECIFY | Tools, folders, data flow, configuration, traceability chain |
| 4 | Agents | [`../AGENTS.md`](../AGENTS.md) | all | What AI may and may not do; integrity rules |
| 5 | Security | [`../SECURITY.md`](../SECURITY.md) | all | Legal scope, NDA, secrets, safe AI use |
| 6 | Code Style | [`CODE-STYLE.md`](CODE-STYLE.md) + `.editorconfig`, `.prettierrc`, `pyproject.toml` | BUILD | Formatting and conventions |
| 7 | SQA | [`SQA-STRATEGY.md`](SQA-STRATEGY.md) + `sqa/02-manual/`, `tests/` | SPECIFY / TEST | Test levels, severity, exit criteria, AI policy |
| 8 | README | [`../README.md`](../sqa/README.md) | all | Front page: what, how to run, results |

Extra documents specific to this portfolio:

| Document | Purpose |
|---|---|
| [`CONFIDENTIALITY-WORKFLOW.md`](CONFIDENTIALITY-WORKFLOW.md) | Separates authorized work in the official project repository from approved, sanitized public portfolio evidence |
| [`thinking/`](thinking) | Strategic, metacognitive, and critical-thinking logs |
| [`../sqa/ai-testing/`](../sqa/ai-testing) | Delegation rules, verification gate, AI-test log and precision |
| [`../PUBLISH-CHECKLIST.md`](../PUBLISH-CHECKLIST.md) | Final gate before the repo goes public |
