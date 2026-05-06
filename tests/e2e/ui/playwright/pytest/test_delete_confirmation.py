import pytest

def test_delete_confirmation_cancel_keeps_task(chrome_page, app_base_url):
    """TC-DEL-CONF-001: Clicking 'Cancel' on confirmation dialog does NOT delete task"""
    page = chrome_page
    
    # 1. Add a task
    page.goto(f"{app_base_url}/tasks/new")
    page.fill('input[name="title"]', "Task to Keep")
    page.click('button[type="submit"]')
    
    # 2. Verify task exists
    assert "Task to Keep" in page.content()
    
    # 3. Click delete button and dismiss (Cancel) the confirmation
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.click('button.btn-delete')
    
    # 4. Wait a moment and verify task still exists
    page.wait_for_timeout(500)
    assert "Task to Keep" in page.content()


def test_delete_confirmation_confirm_deletes_task(chrome_page, app_base_url):
    """TC-DEL-CONF-002: Clicking 'OK' on confirmation dialog DOES delete task"""
    page = chrome_page
    
    # 1. Add a task
    page.goto(f"{app_base_url}/tasks/new")
    page.fill('input[name="title"]', "Task to Delete")
    page.click('button[type="submit"]')
    
    # 2. Verify task exists
    assert "Task to Delete" in page.content()
    
    # 3. Click delete button and accept (OK) the confirmation
    page.on("dialog", lambda dialog: dialog.accept())
    page.click('button.btn-delete')
    
    # 4. Wait for page reload and verify task is gone
    page.wait_for_timeout(500)
    assert "Task to Delete" not in page.content()


def test_delete_confirmation_dialog_text(chrome_page, app_base_url):
    """TC-DEL-CONF-003: Verify confirmation dialog shows expected message"""
    page = chrome_page
    
    # 1. Add a task
    page.goto(f"{app_base_url}/tasks/new")
    page.fill('input[name="title"]', "Test Task")
    page.click('button[type="submit"]')
    
    # 2. Set up dialog handler to capture the message
    dialog_message = []
    page.on("dialog", lambda dialog: dialog_message.append(dialog.message) or dialog.dismiss())
    
    # 3. Click delete button
    page.click('button.btn-delete')
    
    # 4. Verify dialog message
    assert "Are you sure you want to delete this task?" in dialog_message[0]