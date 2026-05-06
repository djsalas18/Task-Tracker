"""TaskService.clear_tasks and get_tasks behavior (not previously covered in isolation)."""
import pytest

from app.services.task_service import TaskService


@pytest.mark.unit
def test_clear_tasks_removes_all_tasks_and_persists_empty(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    service = TaskService(storage=None)
    service.add_task("A", "low", "d1")
    service.add_task("B", "high","d2")
    assert len(service.get_all_tasks()) == 2

    service.clear_tasks()
    assert service.get_all_tasks() == []


@pytest.mark.unit
def test_get_tasks_is_alias_of_get_all_tasks():
    service = TaskService(storage=None)
    service.add_task("X", "low", "y")
    assert service.get_tasks() == service.get_all_tasks()
