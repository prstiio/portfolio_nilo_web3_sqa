# Delegation rules

Delegate when all three hold: the result is **machine-verifiable**, the action is **reversible**, and the **impact of an error is low**. Otherwise the owner does it.

| Task | AI may draft | Owner decides | Why |
|---|---|---|---|
| Boilerplate (page object skeleton, fixtures) | Yes | Reviews diff | Compiler, linter and a run verify it |
| Test case candidates from a requirement | Yes | Selects, edits, sets expected result | The test oracle is a human judgment |
| Selectors / locator suggestions | Yes | Checks against the real DOM | Fails loudly when wrong |
| Test data variations (boundary values) | Yes | Confirms the boundary itself | Derived from the spec, spot-checkable |
| Explaining a stack trace | Yes | Confirms the root cause by reproducing | Plausible-sounding is not proven |
| Bug report wording | Yes (polish) | Observes the bug, assigns severity | AI cannot observe the SUT |
| Test strategy and priorities | Ideas only | Yes | Needs business context and risk appetite |
| Expected results / oracle | No (suggest only) | Yes | An AI-written oracle copies the bug into the test |
| Severity and priority | No | Yes | Business impact judgment |
| Security findings and exploit work | No | Yes | Legal scope and harm (see SECURITY.md) |
| Anything involving real money or private data | No | Yes | Irreversible |
| Publishing numbers (pass rate, precision) | No | Yes, from a command output | Evidence, not prose |

## Red flags that mean "stop delegating"
- The AI states a result you did not run or see.
- Tests pass on the first try and you cannot say why they could fail.
- You cannot explain a line of the generated test to an interviewer.
