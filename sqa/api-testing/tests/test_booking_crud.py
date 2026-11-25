import pytest
from jsonschema import validate

from utils.data import booking_payload
from utils.schemas import BOOKING_SCHEMA, CREATE_BOOKING_SCHEMA


@pytest.mark.smoke
@pytest.mark.schema
def test_create_booking_returns_id_and_matches_schema(client, token):
    """TC-API-004: creating a booking returns an id and a contract-valid body."""
    payload = booking_payload()
    resp = client.post("/booking", json=payload)
    try:
        assert resp.status_code == 200
        body = resp.json()
        validate(body, CREATE_BOOKING_SCHEMA)
        assert body["booking"]["firstname"] == payload["firstname"]
    finally:
        if resp.status_code == 200:
            client.delete(
                f"/booking/{resp.json()['bookingid']}", headers={"Cookie": f"token={token}"}
            )


@pytest.mark.regression
@pytest.mark.schema
def test_get_booking_returns_what_was_created(client, booking):
    """TC-API-005: reading a booking returns the stored data."""
    resp = client.get(f"/booking/{booking['id']}")

    assert resp.status_code == 200
    body = resp.json()
    validate(body, BOOKING_SCHEMA)
    assert body["firstname"] == booking["payload"]["firstname"]
    assert body["totalprice"] == booking["payload"]["totalprice"]


@pytest.mark.regression
def test_list_bookings_contains_created_id(client, booking):
    """TC-API-006: the booking list includes a newly created booking."""
    resp = client.get("/booking")

    assert resp.status_code == 200
    assert booking["id"] in [item["bookingid"] for item in resp.json()]


@pytest.mark.regression
def test_update_booking_changes_the_stored_values(client, token, booking):
    """TC-API-007: PUT with a valid token replaces the booking."""
    updated = booking_payload(firstname="Updated", totalprice=999)
    resp = client.put(
        f"/booking/{booking['id']}", json=updated, headers={"Cookie": f"token={token}"}
    )

    assert resp.status_code == 200
    assert resp.json()["firstname"] == "Updated"
    # verify persistence with an independent read, not only the PUT response
    assert client.get(f"/booking/{booking['id']}").json()["totalprice"] == 999


@pytest.mark.regression
def test_partial_update_changes_only_sent_fields(client, token, booking):
    """TC-API-008: PATCH changes only the fields sent."""
    resp = client.request(
        "PATCH",
        f"/booking/{booking['id']}",
        json={"lastname": "Patched"},
        headers={"Cookie": f"token={token}"},
    )

    assert resp.status_code == 200
    body = resp.json()
    assert body["lastname"] == "Patched"
    assert body["firstname"] == booking["payload"]["firstname"]


@pytest.mark.regression
def test_delete_booking_removes_it(client, token, booking):
    """TC-API-009: DELETE with a valid token removes the booking."""
    resp = client.delete(f"/booking/{booking['id']}", headers={"Cookie": f"token={token}"})

    assert resp.status_code == 201  # documented behavior of this API
    assert client.get(f"/booking/{booking['id']}").status_code == 404
