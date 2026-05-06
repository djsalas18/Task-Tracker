"""Integration: GET /api/time response contract (Sprint 2 TimeService on the wire)."""
import pytest


@pytest.mark.integration
def test_get_time_returns_json_status_200_and_payload_shape(client):
    response = client.get("/api/time")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "utc_datetime" in data or "error" in data
