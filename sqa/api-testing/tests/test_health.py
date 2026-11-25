import pytest


@pytest.mark.smoke
def test_health_check_responds(client):
    """TC-API-001: health endpoint reports the service is up."""
    resp = client.get("/ping")

    assert resp.status_code == 201  # documented behavior of this API (unusual but intended)
