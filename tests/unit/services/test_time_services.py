import pytest
from app.services.time_service import TimeService
from tests.mocks.mock_http_client import MockHTTPClient

@pytest.mark.unit
def test_time_service_with_mock():

    service = TimeService(http_client=MockHTTPClient())

    result = service.get_current_time()

    assert result["utc_datetime"] == "2025-01-01T12:00:00"