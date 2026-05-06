import pytest
import requests

BASE_URL = "http://localhost:5000"

@pytest.mark.external
def test_api_time_returns_200():
    """TC-TIME-001: /api/time endpoint returns 200 OK"""
    response = requests.get(f"{BASE_URL}/api/time")
    assert response.status_code == 200


@pytest.mark.external
def test_api_time_returns_valid_utc_format():
    """TC-TIME-002: /api/time returns valid UTC datetime format"""
    response = requests.get(f"{BASE_URL}/api/time")
    data = response.json()
    
    # Should have utc_datetime field
    assert "utc_datetime" in data
    
    # Should look like ISO format with Z
    utc_time = data["utc_datetime"]
    assert "Z" in utc_time or "T" in utc_time


@pytest.mark.external
def test_api_time_has_source_field():
    """TC-TIME-003: /api/time indicates data source"""
    response = requests.get(f"{BASE_URL}/api/time")
    data = response.json()
    
    assert "source" in data
    # Source should indicate where time came from (external or fallback)
    assert "External" in data["source"] or "Fallback" in data["source"]
