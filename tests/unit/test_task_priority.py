import pytest
from app.services.task_service import TaskService

def test_add_task_with_low_priority():
    """Test adding task with low priority"""
    service = TaskService(storage=None)
    
    # Signature: add_task(title, priority, description=None)
    task = service.add_task("Low Priority Task", "low", "Test description")
    
    assert task["priority"] == "low"
    assert task["title"] == "Low Priority Task"


def test_add_task_with_medium_priority():
    """Test adding task with medium priority"""
    service = TaskService(storage=None)
    
    task = service.add_task("Medium Priority Task", "medium", "Test description")
    
    assert task["priority"] == "medium"


def test_add_task_with_high_priority():
    """Test adding task with high priority"""
    service = TaskService(storage=None)
    
    task = service.add_task("High Priority Task", "high", "Test description")
    
    assert task["priority"] == "high"


def test_add_task_without_description():
    """Test adding task with priority but no description"""
    service = TaskService(storage=None)
    
    # description is optional (defaults to None)
    task = service.add_task("Task No Desc", "medium")
    
    assert task["priority"] == "medium"
    assert task["title"] == "Task No Desc"
    assert task["description"] is None or task["description"] == ""


def test_add_task_invalid_priority_raises_error():
    """Test that invalid priority raises ValueError"""
    service = TaskService(storage=None)
    
    with pytest.raises(ValueError, match="Priority must be low, medium, or high"):
        service.add_task("Invalid Task", "urgent", "Description")


def test_get_tasks_include_priority_field():
    """Test that returned tasks include priority field"""
    service = TaskService(storage=None)
    
    service.add_task("Priority Task", "high", "Desc")
    tasks = service.get_tasks()
    
    assert len(tasks) > 0
    assert "priority" in tasks[0]
    assert tasks[0]["priority"] == "high"


def test_get_tasks_sorted_by_priority_ascending():
    """Test tasks are sorted by priority (low → medium → high)"""
    service = TaskService(storage=None)
    
    # Add tasks in random order
    service.add_task("High Task", "high", "Desc")
    service.add_task("Low Task", "low", "Desc")
    service.add_task("Medium Task", "medium", "Desc")
    
    tasks = service.get_tasks()
    priorities = [t["priority"] for t in tasks]
    
    expected = ["high", "low", "medium"]
    assert priorities == expected


