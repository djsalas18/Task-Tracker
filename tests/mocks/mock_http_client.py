class MockHTTPClient:
    """
    Mock HTTP client used for automated testing.
    Simulates the behavior of the external Time API.
    """

    def get(self, url, timeout=3, headers=None):

        class MockResponse:

            def raise_for_status(self):
                pass

            def json(self):
                return {"dateTime": "2025-01-01T12:00:00"}

        return MockResponse()
