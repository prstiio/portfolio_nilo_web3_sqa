import pytest


@pytest.mark.smoke
def test_valid_credentials_return_token(client):
    """TC-API-002: valid credentials return a token."""
    resp = client.post("/auth", json={"username": "admin", "password": "password123"})

    assert resp.status_code == 200
    assert resp.json().get("token")


@pytest.mark.negative
def test_invalid_credentials_return_no_token(client):
    """TC-API-003: invalid credentials do not return a token."""
    resp = client.post("/auth", json={"username": "admin", "password": "wrong"})

    assert resp.status_code == 200  # documented: this API answers 200 with a reason
    body = resp.json()
    assert "token" not in body
    assert body.get("reason") == "Bad credentials"
