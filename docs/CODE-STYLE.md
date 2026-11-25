# Code Style

Consistency beats preference. Formatting is enforced by `.editorconfig`, `.prettierrc` (UI) and `ruff` settings (API). Naming and structure: [`DESIGN-SYSTEM.md`](DESIGN-SYSTEM.md).

## General
- English identifiers and comments.
- One behavior per test. Tests must be independent and runnable in any order.
- No commented-out code. No fixed sleeps.
- Commit messages: `type: short summary` (`docs`, `test`, `fix`, `ci`, `chore`).

## TypeScript / Playwright (`sqa/web-ui-playwright/`)
- 2-space indentation, single quotes, semicolons, trailing commas, 100-char lines (see `.prettierrc`).
- Prefer user-facing locators: `getByRole`, `getByLabel`, `getByText`; `getByTestId` where the app provides stable test ids (this repo sets `testIdAttribute: 'data-test'`).
- Page objects: `PascalCase` classes, `camelCase` members, `readonly` locators, async methods that describe user intent (`login`, `addToCart`).
- Assertions are web-first (`await expect(locator).toBeVisible()`), never `isVisible()` + `expect(true)`.
- Tags in the test details object: `{ tag: '@smoke' }`, `{ tag: '@regression' }`.
- Link to the manual case: `annotation: { type: 'testcase', description: 'TC-LOGIN-001' }`.
- Use `test.step()` to make reports readable for long flows.

## Python / pytest (`sqa/api-testing/`)
- 4-space indentation, `snake_case`, type hints on helpers, line length 100 (see `pyproject.toml`).
- Test names: `test_<what>_<condition>_<expected>`.
- Fixtures in `conftest.py`; create/cleanup resources in fixtures (yield), not inside tests.
- Assert status code **and** body shape (schema) **and** key fields.
- Mark tests with the registered markers only: `smoke`, `regression`, `negative`, `schema`.
- Put the TC id at the start of the docstring: `"""TC-API-006: reading a booking returns what was created."""`.

## Markdown
- One H1 per file. Tables for structured data. Relative links.
- Keep `TODO` / `EXAMPLE` markers until content is verified.
