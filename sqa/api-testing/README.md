# API testing — pytest + requests + jsonschema

Target: [Restful-Booker](https://restful-booker.herokuapp.com), a public API built for test practice (see [SECURITY.md](../../SECURITY.md)).

## Run

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
pytest                         # all tests
pytest -m smoke                # smoke only
pytest -m "negative"           # negative only
ruff check . && ruff format --check .
```

Reports: `reports/junit.xml` and `reports/report.html` (git-ignored; CI uploads them as artifacts).

## Offline / framework self-test

```bash
python tools/mock_booker.py 3001 &
BASE_URL=http://127.0.0.1:3001 pytest
```

`tools/mock_booker.py` is a stdlib stand-in that encodes only behavior the public API documents.
A green run against it proves the framework works. It is **not** evidence about the real service.

## Conventions
- One behavior per test; each test docstring starts with its manual case id, e.g. `"""TC-API-007: ..."""`. A letter suffix (`TC-API-007b`) is allowed for variants.
- Markers are registered in `pytest.ini` and enforced by `--strict-markers`: `smoke`, `regression`, `negative`, `schema`. Do not invent others without registering them.
- Fixtures create and clean up their own data (`booking`), so tests never depend on each other.
- Assertions per API test: status code, body/contract, and an independent read-back when state changes.
- Quirks of the documented API (ping returns 201, bad credentials return 200 with a reason, invalid POST returns 500) are asserted as documented and called out in comments.

## Coverage
| Area | Tests |
|---|---|
| Health | TC-API-001 |
| Auth | TC-API-002, 003 |
| Booking CRUD + contract | TC-API-004 … 009, 016 |
| Authorization and negative input | TC-API-010 … 015 |

Status: not yet executed against the real API from this repository's build environment. See [sqa/05-reports](../05-reports).
