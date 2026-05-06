"""
Sprint 2: TimeService uses an injectable http_client (app/services/time_service.py).
Unit coverage: success path, network failure -> UTC fallback, malformed external response handling.
"""
import pytest
from unittest.mock import MagicMock, patch

from app.services.time_service import TimeService
from tests.mocks.mock_http_client import MockHTTPClient


@pytest.mark.unit
def test_get_current_time_uses_injected_client_success_path():
    service = TimeService(http_client=MockHTTPClient())
    result = service.get_current_time()
    assert result["utc_datetime"] == "2025-01-01T12:00:00"
    assert result["source"] == "TimeAPI.io (External)"


@pytest.mark.unit
def test_get_current_time_falls_back_when_http_client_raises():
    class BrokenClient:
        def get(self, *args, **kwargs):
            raise ConnectionError("simulated network failure")

    service = TimeService(http_client=BrokenClient())
    result = service.get_current_time()
    assert "utc_datetime" in result
    assert result["source"] == "System Time (Fallback)"


@pytest.mark.unit
def test_get_current_time_uses_utc_string_format_on_fallback():
    class BrokenClient:
        def get(self, *args, **kwargs):
            raise TimeoutError("timeout")

    with patch("app.services.time_service.datetime") as mock_dt:
        mock_now = MagicMock()
        mock_now.strftime.return_value = "2030-06-15T00:00:00.000000Z"
        mock_dt.utcnow.return_value = mock_now
        result = TimeService(http_client=BrokenClient()).get_current_time()
    assert result["source"] == "System Time (Fallback)"
    assert result["utc_datetime"] == "2030-06-15T00:00:00.000000Z"
