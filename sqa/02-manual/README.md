# 02 — Manual Testing

| File | Purpose |
|---|---|
| [`test-cases.md`](test-cases.md) | Readable test case catalogue (source of truth) |
| [`test-cases.csv`](test-cases.csv) | Same cases in CSV for Excel / Google Sheets / TestRail |
| [`execution-log.md`](execution-log.md) | Results of each manual run, with evidence |
| [`exploratory-sessions/`](exploratory-sessions) | Session-based exploratory testing notes |
| [`non-functional-checklist.md`](non-functional-checklist.md) | Accessibility, performance, security-awareness, compatibility |

## How to work
1. Write cases from requirements ([`../sqa/01-planning/01-requirements.md`](../01-planning/01-requirements.md)). Every case references ≥ 1 `REQ-` ID.
2. Mix positive, negative, boundary, and edge cases. Suggested mix (a rule of thumb, adjust to risk): about half positive, a third negative, the rest boundary/edge. Tiers: P0 ≈ 20 cases, P1 = 40–80.
3. Execute each case manually. Record real results in the execution log. Status stays `Not Run` until executed.
4. Failures → file a bug in [`../sqa/03-bug-reports/`](../03-bug-reports) and link it here.
5. Mark `Automated?` and update the traceability matrix when you automate a case.

## Test case quality checklist
- [ ] Title states the behavior being verified
- [ ] Preconditions are explicit
- [ ] Steps are atomic and repeatable by someone else
- [ ] Expected result is observable and specific
- [ ] Test data is listed
- [ ] Linked requirement and priority are set
