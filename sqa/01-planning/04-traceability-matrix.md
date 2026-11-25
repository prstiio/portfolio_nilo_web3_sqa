# 04 — Traceability Matrix

Maps **requirement → manual test case → automated test → latest result**. The automated link is checked by `python scripts/portfolio_status.py`: it fails on references to unknown IDs and lists requirements without test cases.

Legend — Result: `Pass` / `Fail` / `Blocked` / `Not Run`. Only fill after real execution.

| Requirement | Test case(s) | Automated in | Result | Bugs |
|---|---|---|---|---|
| REQ-LOGIN-01 | TC-LOGIN-001 | `sqa/web-ui-playwright/tests/login.spec.ts` | Not Run | — |
| REQ-LOGIN-02 | TC-LOGIN-002, TC-LOGIN-007 | `sqa/web-ui-playwright/tests/login.spec.ts` | Not Run | — |
| REQ-LOGIN-03 | TC-LOGIN-003, TC-LOGIN-004 | `sqa/web-ui-playwright/tests/login.spec.ts` | Not Run | — |
| REQ-LOGIN-04 | TC-LOGIN-005 | `sqa/web-ui-playwright/tests/login.spec.ts` | Not Run | — |
| REQ-LOGIN-05 | TC-LOGIN-006 | — (manual only) | Not Run | — |
| REQ-INV-01 | TODO | — | Not Run | — |
| REQ-INV-02 | TC-INV-001, TC-INV-002 | `sqa/web-ui-playwright/tests/inventory.spec.ts` | Not Run | — |
| REQ-CART-01 | TC-CART-001 | `sqa/web-ui-playwright/tests/inventory.spec.ts` | Not Run | — |
| REQ-CART-02 | TC-CART-002 | `sqa/web-ui-playwright/tests/inventory.spec.ts` | Not Run | — |
| REQ-CHK-01 | TC-CHK-001 | `sqa/web-ui-playwright/tests/cart-checkout.spec.ts` | Not Run | — |
| REQ-CHK-02 | TC-CHK-002 | `sqa/web-ui-playwright/tests/cart-checkout.spec.ts` | Not Run | — |
| REQ-API-01 | TC-API-001 | `sqa/api-testing/tests/test_health.py` | Not Run | — |
| REQ-API-02 | TC-API-002, TC-API-003 | `sqa/api-testing/tests/test_auth.py` | Not Run | — |
| REQ-API-03 | TC-API-004, 005, 006, 007, 008, 009, 013, 014, 015, 016 | `sqa/api-testing/tests/test_booking_crud.py`, `test_booking_negative.py` | Not Run | — |
| REQ-API-04 | TC-API-010, 011, 012 | `sqa/api-testing/tests/test_booking_negative.py` | Not Run | — |

## Coverage summary (copy from `python scripts/portfolio_status.py`)
| Metric | Value |
|---|---|
| Requirements with ≥ 1 test case | TODO |
| Test cases referenced by an automated test | TODO |
| Requirements with all linked tests passing | TODO |
