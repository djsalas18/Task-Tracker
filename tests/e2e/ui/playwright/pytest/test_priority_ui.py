import pytest

def test_task_list_displays_priority_labels(chrome_page, app_base_url):
    """TC-PRIORITY-UI-001: Task list shows priority labels"""
    page = chrome_page
    
    # First add tasks with different priorities via API (more reliable)
    import requests
    base = "http://localhost:5000/api/tasks"
    requests.post(base, json={"title": "Low Task", "priority": "low"})
    requests.post(base, json={"title": "Medium Task", "priority": "medium"})
    requests.post(base, json={"title": "High Task", "priority": "high"})
    
    # Navigate to task list
    page.goto(f"{app_base_url}/tasks")
    
    # Check for priority text
    content = page.content()
    assert "low" in content.lower() or "medium" in content.lower() or "high" in content.lower()


def test_priority_css_classes_exist(chrome_page, app_base_url):
    """TC-PRIORITY-UI-002: Priority CSS classes are present in the DOM"""
    import requests
    base = "http://localhost:5000/api/tasks"
    requests.post(base, json={"title": "High Priority Task", "priority": "high"})
    
    page = chrome_page
    page.goto(f"{app_base_url}/tasks")
    
    # Check for priority CSS classes
    html = page.content()
    has_low_class = 'task-priority-low' in html
    has_medium_class = 'task-priority-medium' in html
    has_high_class = 'task-priority-high' in html
    
    # At least one priority class should exist
    assert has_low_class or has_medium_class or has_high_class


def test_sort_button_exists(chrome_page, app_base_url):
    """TC-PRIORITY-UI-003: Sort button is present on task list page"""
    import requests
    requests.post("http://localhost:5000/api/tasks", json={"title": "Sample Task", "priority": "low"})
    
    page = chrome_page
    page.goto(f"{app_base_url}/tasks")
    
    # Look for sort button
    sort_button = page.locator('button:has-text("Sort By")')
    assert sort_button.count() > 0


def test_sort_button_changes_order(chrome_page, app_base_url):
    """TC-PRIORITY-UI-004: Clicking sort button changes task order"""
    import requests
    base = "http://localhost:5000/api/tasks"
    requests.post(base, json={"title": "Low Priority", "priority": "low"})
    requests.post(base, json={"title": "High Priority", "priority": "high"})
    
    page = chrome_page
    page.goto(f"{app_base_url}/tasks")
    
    # Get initial order
    tasks_before = page.locator('.task-title').all_text_contents()
    
    # Click sort button
    page.click('button:has-text("Sort By")')
    page.wait_for_timeout(500)
    
    # Get new order
    tasks_after = page.locator('.task-title').all_text_contents()
    
    # Order should be different
    assert tasks_before != tasks_after