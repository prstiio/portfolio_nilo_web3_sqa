# Prompt templates

Give the model the context a tester would need. Never paste secrets, NDA material or real user data.

## P1 — Test case candidates from a requirement
```
Role: senior QA engineer.
Requirement: <paste REQ text>
Known behavior (observed by me): <bullets>
Output: a table of test cases (title, preconditions, steps, expected result, type F/N/B).
Constraints: use equivalence partitioning and boundary values; no more than 8 cases;
flag any expected result you are unsure about as "NEEDS OWNER".
```

## P2 — Playwright test from an existing manual case
```
Context: Playwright + TypeScript, Page Object Model, fixtures in fixtures/index.ts,
locators by role/label/test id, web-first assertions, no waitForTimeout.
Manual case: <paste TC row>
Existing page objects: <paste signatures only>
Output: one test file section with annotation {type:'testcase', description:'TC-...'}.
Do not invent locators: if you need one, list it under "LOCATORS TO CONFIRM".
```

## P3 — pytest test from an API case
```
Context: pytest + requests, fixtures client/token/booking in conftest.py, markers
smoke/regression/negative/schema only. Docstring starts with the TC id.
Case: <paste TC row>
Documented behavior: <paste from API docs>
Output: test function(s) with status, body/contract, and read-back assertions.
```

## P4 — Review my test (adversarial)
```
Here is a test and the requirement it should verify. List ways this test could pass while
the feature is broken. Do not rewrite it; list at most 5 weaknesses, most serious first.
```

## P5 — Bug report polish
```
Rewrite this bug report for clarity. Keep every fact exactly as written; do not add steps,
causes or severity. Return the same template fields.
```
