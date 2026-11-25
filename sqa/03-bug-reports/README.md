# 03 — Bug Reports

Only **real, reproduced** defects belong here. Quality beats quantity: a precise report that a developer can act on in two minutes is the goal.

## How to file
1. Reproduce at least twice. Check it isn't a duplicate (see [`index.md`](index.md)).
2. Copy [`_TEMPLATE.md`](_TEMPLATE.md) → `BUG-NNN-short-title.md`.
3. Attach evidence (screenshot / recording / HAR / logs) in [`evidence/`](evidence) and link it.
4. Add a row to [`index.md`](index.md) and link the bug from the failing test case in [`../sqa/02-manual/`](../02-manual).
5. If the target is a third-party product, **report privately to the owner first** and do not publish details until fixed (see [`../SECURITY.md`](../../SECURITY.md)). Never publish NDA/crowdtesting content.
6. Separate **facts** (what you observed) from **hypotheses** (what might cause it).

## Severity & priority
See [`../docs/SQA-STRATEGY.md`](../../docs/SQA-STRATEGY.md#5-severity--priority).

## Good bug report checklist
- [ ] Title = **what** is wrong **where** (not "doesn't work")
- [ ] Environment: browser + version, OS, build/URL, date
- [ ] Minimal, numbered steps to reproduce, starting from a clean state
- [ ] Expected vs actual result
- [ ] Evidence attached
- [ ] Severity and priority justified
- [ ] Frequency (always / intermittent) and workaround noted
- [ ] Linked requirement / test case
- [ ] No sensitive data in screenshots or logs
