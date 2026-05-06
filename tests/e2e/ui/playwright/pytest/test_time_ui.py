import pytest

def test_time_page_loads(chrome_page, app_base_url):
    """TC-TIME-004: /time page loads successfully"""
    page = chrome_page
    page.goto(f"{app_base_url}/time")
    
    # Page should load
    assert page.title() == "Task Tracker"
    assert "UTC Time" in page.content()


def test_time_page_displays_utc_time(chrome_page, app_base_url):
    """TC-TIME-005: Time page shows UTC time value"""
    page = chrome_page
    page.goto(f"{app_base_url}/time")
    
    # Should show time data
    content = page.content()
    assert "UTC Time:" in content
    # Look for timestamp-like pattern (numbers, colons, dashes, Z)
    import re
    time_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
    assert re.search(time_pattern, content) or "[MOCK" in content


def test_time_page_has_back_link(chrome_page, app_base_url):
    """TC-TIME-006: Time page has Back to Home link"""
    page = chrome_page
    page.goto(f"{app_base_url}/time")
    
    back_link = page.locator('a:has-text("Back to Home")')
    assert back_link.count() > 0


def test_navigation_to_time_from_home(chrome_page, app_base_url):
    """TC-TIME-007: Can navigate to time page from navigation menu"""
    page = chrome_page
    page.goto(f"{app_base_url}/")
    
    # Find and click Time link in nav
    page.click('nav a:has-text("Time (UTC)")')
    
    # Should be on time page
    assert "/time" in page.url
    assert "UTC Time" in page.content()