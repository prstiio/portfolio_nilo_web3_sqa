import os
from collections.abc import Iterator

import pytest
from dotenv import load_dotenv

from utils.client import ApiClient
from utils.data import booking_payload

load_dotenv()


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://restful-booker.herokuapp.com").rstrip("/")


@pytest.fixture(scope="session")
def client(base_url: str) -> ApiClient:
    return ApiClient(base_url, timeout=float(os.getenv("REQUEST_TIMEOUT", "15")))


@pytest.fixture(scope="session")
def token(client: ApiClient) -> str:
    resp = client.post(
        "/auth",
        json={
            "username": os.getenv("API_USER", "admin"),
            "password": os.getenv("API_PASSWORD", "password123"),
        },
    )
    assert resp.status_code == 200, f"auth failed: {resp.status_code} {resp.text}"
    value = resp.json().get("token")
    assert value, "auth response had no token"
    return value


@pytest.fixture
def booking(client: ApiClient, token: str) -> Iterator[dict]:
    """A disposable booking: created before the test, deleted after it."""
    payload = booking_payload()
    resp = client.post("/booking", json=payload)
    assert resp.status_code == 200, f"setup failed: {resp.status_code} {resp.text}"
    created = resp.json()
    yield {"id": created["bookingid"], "payload": payload}
    client.delete(f"/booking/{created['bookingid']}", headers={"Cookie": f"token={token}"})
