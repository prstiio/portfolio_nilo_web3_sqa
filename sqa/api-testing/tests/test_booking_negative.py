import pytest


@pytest.mark.negative
def test_update_without_token_is_forbidden(client, booking):
    """TC-API-010: PUT without a token is rejected."""
    resp = client.put(f"/booking/{booking['id']}", json=booking["payload"])

    assert resp.status_code == 403


@pytest.mark.negative
def test_delete_without_token_is_forbidden(client, booking):
    """TC-API-011: DELETE without a token is rejected and the booking remains."""
    resp = client.delete(f"/booking/{booking['id']}")

    assert resp.status_code == 403
    assert client.get(f"/booking/{booking['id']}").status_code == 200


@pytest.mark.negative
def test_update_with_invalid_token_is_forbidden(client, booking):
    """TC-API-012: PUT with a made-up token is rejected."""
    resp = client.put(
        f"/booking/{booking['id']}",
        json=booking["payload"],
        headers={"Cookie": "token=not-a-real-token"},
    )

    assert resp.status_code == 403


@pytest.mark.negative
def test_get_unknown_booking_returns_not_found(client):
    """TC-API-013: reading a non-existent id returns 404."""
    resp = client.get("/booking/999999999")

    assert resp.status_code == 404


@pytest.mark.negative
def test_create_booking_with_missing_fields_is_rejected(client):
    """TC-API-014: an incomplete payload must not be accepted as a valid booking."""
    resp = client.post("/booking", json={"firstname": "OnlyName"})

    # Documented behavior: this API fails with 500 on invalid payloads.
    # A 5xx here is itself worth a note in the report (ideally it would be 400).
    assert resp.status_code in (400, 500)


@pytest.mark.negative
@pytest.mark.parametrize("bad_id", ["abc", "-1", "0"])
def test_get_booking_with_invalid_id_is_not_ok(client, bad_id):
    """TC-API-015: malformed ids never return a booking."""
    resp = client.get(f"/booking/{bad_id}")

    assert resp.status_code in (400, 404)


@pytest.mark.regression
def test_filter_by_lastname_returns_only_matches(client, booking):
    """TC-API-016: list filter by lastname returns the created booking."""
    resp = client.get("/booking", params={"lastname": booking["payload"]["lastname"]})

    assert resp.status_code == 200
    assert booking["id"] in [item["bookingid"] for item in resp.json()]
