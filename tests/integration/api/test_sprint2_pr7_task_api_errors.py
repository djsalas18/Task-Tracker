"""Integration: task API error handling (400/404) for routes in app/routes/tasks.py."""
import pytest


@pytest.mark.integration
def test_post_task_missing_title_returns_400(client):
    r = client.post("/api/tasks", json={})
    assert r.status_code == 400
    assert r.get_json()["error"] == "Title is required"


@pytest.mark.integration
def test_post_task_empty_string_title_returns_400(client):
    r = client.post("/api/tasks", json={"title": "   "})
    assert r.status_code == 400
    assert r.get_json()["error"] == "Title is required"


@pytest.mark.integration
def test_put_complete_unknown_task_returns_404(client):
    r = client.put("/api/tasks/9999")
    assert r.status_code == 404
    assert r.get_json()["error"] == "Task not found"


@pytest.mark.integration
def test_delete_unknown_task_returns_404(client):
    r = client.delete("/api/tasks/9999")
    assert r.status_code == 404
    assert r.get_json()["error"] == "Task not found"


@pytest.mark.integration
def test_post_reset_returns_200_and_message(client):
    r = client.post("/api/tasks/reset")
    assert r.status_code == 200
    assert "message" in r.get_json()


@pytest.mark.integration
def test_post_task_missing_priority_returns_400(client):
    r = client.post("/api/tasks", json={"title": "Task Title"})
    assert r.status_code == 400
    assert r.get_json()["error"] == "Priority is required"


@pytest.mark.integration
def test_post_task_empty_string_priority_returns_400(client):
    r = client.post("/api/tasks", json={"title": "Task Title", "priority":""})
    assert r.status_code == 400
    assert r.get_json()["error"] == "Priority is required"