# tests/tasks/test_add_task.py
import pytest
from flask.testing import FlaskClient

@pytest.mark.unit
def test_add_valid_task(client: FlaskClient):
    """
    TC-US002-001
    """
    # Act - Send valid task
    response = client.post('/api/tasks', json={
        "title": "Test Task",
        "priority": "low",
        "description": "This is a test task."
    })

    # Assert - Response status and fields
    assert response.status_code == 201, "Expected 201 Created for valid task"
    data = response.get_json()
    assert data["title"] == "Test Task"
    assert data["priority"] == "low"
    assert data["description"] == "This is a test task."
    assert "id" in data

# TC US002-002 Missing Title

@pytest.mark.unit
def test_add_task_missing_title(client: FlaskClient):
    """
    TC-US002-002
    """
    # Act
    response = client.post('/api/tasks', json={
        "description": "This is a test task without a title."
    })

    # Assert
    assert response.status_code == 400, "Should return 400 if title is missing"
    data = response.get_json()
    assert isinstance(data, dict)
    assert "error" in data
    assert data["error"] == "Title is required"

@pytest.mark.unit
def test_add_task_empty_title(client: FlaskClient):
    """
    TC-US002-003
    """
    # Act
    response = client.post("/api/tasks", json={
        "title": "",
        "description": "This task has no title"
    })

    # Assert
    assert response.status_code == 400, "Should reject empty title with 400 status"
    data = response.get_json()
    assert isinstance(data, dict)
    assert "error" in data
    assert data["error"] == "Title is required"

@pytest.mark.unit
def test_add_task_empty_priority(client: FlaskClient):
    # Act
    response = client.post("/api/tasks", json={
        "title": "Task Title",
        "priority": '',
        "description": "This task has no title"
    })

    # Assert
    assert response.status_code == 400, "Should reject empty title with 400 status"
    data = response.get_json()
    assert isinstance(data, dict)
    assert "error" in data
    assert data["error"] == "Priority is required"