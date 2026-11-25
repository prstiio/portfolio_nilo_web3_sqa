# AI-assisted testing

AI can draft tests quickly. It can also write tests that pass and prove nothing. This folder is the control system: what may be delegated, how every AI output is verified, and how precision is measured instead of guessed.

| File | Purpose |
|---|---|
| [`delegation-rules.md`](delegation-rules.md) | What AI may draft vs what the owner decides |
| [`verification-gate.md`](verification-gate.md) | 5-step gate every AI-generated test must pass |
| [`prompts.md`](prompts.md) | Reusable prompts (with the context they need) |
| [`ai-test-log.csv`](ai-test-log.csv) | One row per AI-generated test (the raw data) |
| [`precision.py`](precision.py) | Computes precision and failure categories from the log |
| [`experiment-report.md`](experiment-report.md) | The write-up, filled only from the log |

Workflow: prompt → AI draft → **gate** → log row → `python sqa/ai-testing/precision.py` → report.
Rows must come from real runs. An empty log is honest; an invented one ends the portfolio's credibility.
