# Test Cases

> Rows marked `EXAMPLE` show the expected level of detail — verify against the SUT, then edit/extend. **Status stays `Not Run` until you actually execute the case.**
> The traceability checker reads the `TC-…` and `REQ-…` ids in the tables below.

**Type:** F = functional · N = negative · B = boundary · U = usability · C = compatibility
**Priority:** H / M / L

## Template (copy for each new case)

| Field | Value |
|---|---|
| ID | TC-<AREA>-<NNN> |
| Title | |
| Requirement(s) | REQ-... |
| Priority / Type | |
| Preconditions | |
| Test data | |
| Steps | 1. … 2. … |
| Expected result | |
| Automated? | No / `file::test name` |
| Status | Not Run |

---

## Login (REQ-LOGIN-*)

| ID | Title | Req | Pri | Type | Preconditions | Steps | Test data | Expected result | Automated? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-LOGIN-001 | EXAMPLE: Login with valid credentials | REQ-LOGIN-01 | H | F | On login page | 1. Enter username 2. Enter password 3. Click Login | standard user | Product list page is displayed | `login.spec.ts` | Not Run |
| TC-LOGIN-002 | EXAMPLE: Login with wrong password | REQ-LOGIN-02 | H | N | On login page | 1. Enter valid username 2. Enter wrong password 3. Click Login | wrong password | Error message shown; user stays on login page | `login.spec.ts` | Not Run |
| TC-LOGIN-003 | EXAMPLE: Login with empty username | REQ-LOGIN-03 | M | N | On login page | 1. Leave username empty 2. Enter password 3. Click Login | password only | "Username is required" style error shown | `login.spec.ts` | Not Run |
| TC-LOGIN-004 | EXAMPLE: Login with empty password | REQ-LOGIN-03 | M | N | On login page | 1. Enter username 2. Leave password empty 3. Click Login | username only | "Password is required" style error shown | `login.spec.ts` | Not Run |
| TC-LOGIN-005 | EXAMPLE: Locked-out user cannot log in | REQ-LOGIN-04 | M | N | On login page | 1. Enter locked-out credentials 2. Click Login | locked-out user | "locked out" error shown; no access | `login.spec.ts` | Not Run |
| TC-LOGIN-006 | EXAMPLE: Logout returns to login page | REQ-LOGIN-05 | M | F | Logged in | 1. Open menu 2. Click Logout | standard user | Login page displayed; product page not accessible via back button | — | Not Run |
| TC-LOGIN-007 | EXAMPLE: Direct URL access to product page without login | REQ-LOGIN-02 | H | N | Logged out | 1. Open product page URL directly | — | Access denied / redirected to login | `login.spec.ts` | Not Run |

## Inventory (REQ-INV-*)

| ID | Title | Req | Pri | Type | Preconditions | Steps | Test data | Expected result | Automated? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-INV-001 | EXAMPLE: Sort by price low to high | REQ-INV-02 | M | F | Logged in | 1. Select "Price (low to high)" | — | Prices are in ascending order | `inventory.spec.ts` | Not Run |
| TC-INV-002 | EXAMPLE: Sort by name Z to A | REQ-INV-02 | M | F | Logged in | 1. Select "Name (Z to A)" | — | Names are in descending order | `inventory.spec.ts` | Not Run |

## Cart (REQ-CART-*)

| ID | Title | Req | Pri | Type | Preconditions | Steps | Test data | Expected result | Automated? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-CART-001 | EXAMPLE: Add product updates cart badge | REQ-CART-01 | H | F | Logged in, cart empty | 1. Click add-to-cart on a product | any product | Badge shows 1; button changes to Remove | `inventory.spec.ts` | Not Run |
| TC-CART-002 | EXAMPLE: Remove product from cart | REQ-CART-02 | M | F | Cart has 1 item | 1. Click Remove | — | Badge disappears; item gone | `inventory.spec.ts` | Not Run |

## Checkout (REQ-CHK-*)

| ID | Title | Req | Pri | Type | Preconditions | Steps | Test data | Expected result | Automated? | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TC-CHK-001 | EXAMPLE: Checkout requires customer info | REQ-CHK-01 | H | N | Cart has 1 item, on checkout step one | 1. Leave all fields empty 2. Click Continue | — | Validation error shown; cannot proceed | `cart-checkout.spec.ts` | Not Run |
| TC-CHK-002 | EXAMPLE: Complete purchase end-to-end | REQ-CHK-02 | H | F | Logged in | 1. Add item 2. Open cart 3. Checkout 4. Fill info 5. Continue 6. Finish | synthetic customer | Confirmation message displayed | `cart-checkout.spec.ts` | Not Run |

## API (REQ-API-*)

| ID | Title | Req | Pri | Type | Expected result | Automated? | Status |
|---|---|---|---|---|---|---|---|
| TC-API-001 | EXAMPLE: Health check responds | REQ-API-01 | M | F | Status 201 (documented) | `test_health.py` | Not Run |
| TC-API-002 | EXAMPLE: Auth with valid credentials returns token | REQ-API-02 | H | F | Token present | `test_auth.py` | Not Run |
| TC-API-003 | EXAMPLE: Auth with invalid credentials gives no token | REQ-API-02 | H | N | No token; reason 'Bad credentials' | `test_auth.py` | Not Run |
| TC-API-004 | EXAMPLE: Create booking returns id and valid contract | REQ-API-03 | H | F | Booking created; data echoed; matches schema | `test_booking_crud.py` | Not Run |
| TC-API-005 | EXAMPLE: Get booking by id returns stored data | REQ-API-03 | H | F | Same data as created; matches schema | `test_booking_crud.py` | Not Run |
| TC-API-006 | EXAMPLE: List bookings includes the new id | REQ-API-03 | M | F | Created id is in the list | `test_booking_crud.py` | Not Run |
| TC-API-007 | EXAMPLE: Full update with valid token | REQ-API-03 | H | F | Fields replaced; read-back confirms | `test_booking_crud.py` | Not Run |
| TC-API-008 | EXAMPLE: Partial update changes only sent fields | REQ-API-03 | M | F | Only sent fields change | `test_booking_crud.py` | Not Run |
| TC-API-009 | EXAMPLE: Delete booking with valid token | REQ-API-03 | H | F | Booking no longer retrievable (404) | `test_booking_crud.py` | Not Run |
| TC-API-010 | EXAMPLE: Update without token | REQ-API-04 | H | N | 403 Forbidden | `test_booking_negative.py` | Not Run |
| TC-API-011 | EXAMPLE: Delete without token | REQ-API-04 | H | N | 403; booking remains | `test_booking_negative.py` | Not Run |
| TC-API-012 | EXAMPLE: Update with invalid token | REQ-API-04 | H | N | 403 Forbidden | `test_booking_negative.py` | Not Run |
| TC-API-013 | EXAMPLE: Get unknown booking id | REQ-API-03 | M | N | 404 Not Found | `test_booking_negative.py` | Not Run |
| TC-API-014 | EXAMPLE: Create booking with missing fields | REQ-API-03 | M | N | Rejected (400 or documented 500) | `test_booking_negative.py` | Not Run |
| TC-API-015 | EXAMPLE: Get booking with malformed id | REQ-API-03 | L | B | 400 or 404, never a booking | `test_booking_negative.py` | Not Run |
| TC-API-016 | EXAMPLE: Filter bookings by lastname | REQ-API-03 | M | F | Created id is in the filtered list | `test_booking_negative.py` | Not Run |

---

Non-functional checks live in [`non-functional-checklist.md`](non-functional-checklist.md).
