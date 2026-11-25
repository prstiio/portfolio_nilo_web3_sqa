# 01 — Requirements

> When no official requirements exist, **derive** them from observation and state the source. Each requirement must be atomic, testable, and have an ID.
> Rows marked `EXAMPLE` are templates — verify against the real app, then edit or delete.

**Priority:** H = core / must work · M = important · L = nice to have

| ID | Requirement | Priority | Source | Testable? | Status |
|---|---|---|---|---|---|
| REQ-LOGIN-01 | EXAMPLE: A user with valid credentials can log in and reach the product list | H | Observation | Yes | Draft |
| REQ-LOGIN-02 | EXAMPLE: Invalid credentials show an error message and do not grant access | H | Observation | Yes | Draft |
| REQ-LOGIN-03 | EXAMPLE: Username and password are both mandatory (specific message per empty field) | M | Observation | Yes | Draft |
| REQ-LOGIN-04 | EXAMPLE: A locked-out user cannot log in and sees a specific message | M | Observation | Yes | Draft |
| REQ-LOGIN-05 | EXAMPLE: A logged-in user can log out and is returned to the login page | M | Observation | Yes | Draft |
| REQ-INV-01 | EXAMPLE: Product list displays name, price, image, and an add-to-cart action | H | Observation | Yes | Draft |
| REQ-INV-02 | EXAMPLE: Products can be sorted by name (A–Z, Z–A) and price (low–high, high–low) | M | Observation | Yes | Draft |
| REQ-CART-01 | EXAMPLE: Adding a product updates the cart badge count | H | Observation | Yes | Draft |
| REQ-CART-02 | EXAMPLE: A product can be removed from the cart | M | Observation | Yes | Draft |
| REQ-CHK-01 | EXAMPLE: Checkout requires first name, last name, and postal code | H | Observation | Yes | Draft |
| REQ-CHK-02 | EXAMPLE: Completing checkout shows an order confirmation | H | Observation | Yes | Draft |
| REQ-API-01 | EXAMPLE: API health endpoint reports the service is up | M | API docs | Yes | Draft |
| REQ-API-02 | EXAMPLE: Valid credentials return an auth token | H | API docs | Yes | Draft |
| REQ-API-03 | EXAMPLE: A booking can be created, read, updated, and deleted | H | API docs | Yes | Draft |
| REQ-API-04 | EXAMPLE: Modifying/deleting a booking requires authorization | H | API docs | Yes | Draft |

## Non-functional requirements (TODO — make each measurable)
| ID | Requirement | Measure |
|---|---|---|
| NFR-COMPAT-01 | Works on Chromium, Firefox, WebKit | Pass smoke suite on all three |
| NFR-RESP-01 | Usable on a mobile viewport | No blocked core flow on 412×915 |
| NFR-A11Y-01 | Core flows operable by keyboard | Manual checklist passes |
| NFR-PERF-01 | TODO (e.g. product page responds within a stated budget) | TODO |

## Review notes
Ambiguities, missing details, and questions found while reviewing (static testing counts as testing!):
- TODO
