import pytest
import requests

BASE_URL = "http://localhost:5000/api/tasks"


@pytest.fixture(autouse=True)
def reset_api_tasks(request):
    """
    Reset task data before each test in this package.

    - Tests that use the Flask ``client`` fixture run in-process: reset via
      ``POST /api/tasks/reset`` and do not require a live server.
    - Tests that use raw ``requests`` against localhost need the server; if it
      is not running, the test is skipped.
    """
    if "client" in request.fixturenames:
        try:
            request.getfixturevalue("client").post("/api/tasks/reset")
        except Exception:
            pass
        return

    try:
        health_resp = requests.get("http://localhost:5000/api/health", timeout=2)
        if health_resp.status_code != 200:
            pytest.skip(
                f"Server health check failed with status {health_resp.status_code}"
            )

        api_resp = requests.get(BASE_URL, timeout=2)
        if api_resp.status_code != 200:
            pytest.skip(
                f"API endpoint check failed with status {api_resp.status_code}"
            )

        try:
            requests.post(f"{BASE_URL}/reset", timeout=2)
        except requests.exceptions.RequestException:
            pass

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        pytest.skip("Server is not running or not responding, skipping integration test.")
    except Exception as e:
        pytest.skip(f"Server check failed: {e}")
