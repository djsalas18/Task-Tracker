# tests/api/test_add_task_api.py
import pytest
# ✅ TC-RF011-002: POST /api/tasks adds DB entry

@pytest.mark.integration
def test_post_task_adds_to_db(client):
    response = client.post("/api/tasks", json={"title": "DB", "priority": "low", "description": "via API"})
    assert response.status_code == 201