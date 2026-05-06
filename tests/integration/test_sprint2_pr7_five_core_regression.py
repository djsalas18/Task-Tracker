"""
PR-7 five core regression checks (Sprint 2 / ongoing): add, update(complete), delete,
task report (UI), time API. Uses Flask test client; runs with primary pytest selection.
"""
import pytest


@pytest.mark.integration
def test_pr7_add_task(client):
    r = client.post(
        "/api/tasks",
        json={"title": "Sprint2 PR7 add", "priority": "low", "description": "d"},
    )
    assert r.status_code == 201
    assert r.get_json()["title"] == "Sprint2 PR7 add"
    assert r.get_json()["priority"] == "low"


@pytest.mark.integration
def test_pr7_update_task_complete(client):
    client.post("/api/tasks", json={"title": "Sprint2 complete", "priority": "low",})
    r = client.put("/api/tasks/1")
    assert r.status_code == 200
    assert r.get_json()["completed"] is True


@pytest.mark.integration
def test_pr7_delete_task(client):
    client.post("/api/tasks", json={"title": "Sprint2 del", "priority": "low",})
    r = client.delete("/api/tasks/1")
    assert r.status_code == 200
    assert r.get_json()["message"] == "Task deleted"


@pytest.mark.integration
def test_pr7_task_report_page(client):
    client.post("/api/tasks", json={"title": "R1", "priority": "low", "description": "a"})
    r = client.get("/tasks/report")
    assert r.status_code == 200
    assert b"Task Summary Report" in r.data


@pytest.mark.integration
def test_pr7_time_api(client):
    r = client.get("/api/time")
    assert r.status_code == 200
    d = r.get_json()
    assert "utc_datetime" in d or "error" in d
