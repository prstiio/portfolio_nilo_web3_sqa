"""Synthetic payload builders. No real personal data."""

from copy import deepcopy


def booking_payload(**overrides) -> dict:
    payload = {
        "firstname": "Test",
        "lastname": "Customer",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2030-01-01", "checkout": "2030-01-05"},
        "additionalneeds": "Breakfast",
    }
    payload = deepcopy(payload)
    payload.update(overrides)
    return payload
