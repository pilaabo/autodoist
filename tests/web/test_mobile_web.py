import pytest

WEB_BASE_URL = "https://app.todoist.com"


@pytest.mark.web
def test_responsive_layout_mobile(pw_context):
    page = pw_context.new_page(viewport={"width": 375, "height": 812})
    page.goto(WEB_BASE_URL)
    assert page.is_visible("button.hamburger_menu")
