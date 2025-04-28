import os

import pytest

WEB_BASE_URL = "https://app.todoist.com"

TEST_TOKEN = os.getenv("TEST_TOKEN")


@pytest.mark.web
def test_create_task_ui(pw_context):
    page = pw_context.new_page()
    # авторизация через cookie или повторить шаги логина
    page.add_cookie({"name": "token", "value": TEST_TOKEN, "domain": "app.todoist.com"})
    page.goto(f"{WEB_BASE_URL}/today")
    page.click("button.add_task")
    page.fill("textarea.task_editor", "UI task sample")
    page.click("button.submit_task")
    assert page.is_visible("text=UI task sample")


@pytest.mark.web
def test_complete_task_ui(pw_context):
    page = pw_context.new_page()
    page.add_cookie({"name": "token", "value": TEST_TOKEN, "domain": "app.todoist.com"})
    page.goto(f"{WEB_BASE_URL}/today")
    page.click("text=UI task sample")
    page.click("button.complete_task")
    assert page.is_hidden("text=UI task sample")


@pytest.mark.web
def test_move_task_to_project_ui(pw_context):
    page = pw_context.new_page()
    page.add_cookie({"name": "token", "value": TEST_TOKEN, "domain": "app.todoist.com"})
    page.goto(f"{WEB_BASE_URL}/today")
    page.drag_and_drop("text=UI task sample", "#project_inbox")
    assert page.is_visible("#project_inbox >> text=UI task sample")
