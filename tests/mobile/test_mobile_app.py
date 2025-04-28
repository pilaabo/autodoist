import os

import pytest


@pytest.mark.mobile
def test_login_mobile_success(mobile_driver):
    driver = mobile_driver
    driver.find_element("id", "email").send_keys(os.getenv("TEST_EMAIL"))
    driver.find_element("id", "password").send_keys(os.getenv("TEST_PASSWORD"))
    driver.find_element("id", "login_button").click()
    assert driver.find_elements("id", "inbox_view")


@pytest.mark.mobile
def test_add_task_mobile(mobile_driver):
    driver = mobile_driver
    driver.find_element("id", "fab_add_task").click()
    driver.find_element("id", "task_content").send_keys("Mobile task")
    driver.find_element("id", "save_task").click()
    assert driver.find_elements("xpath", "//android.widget.TextView[@text='Mobile task']")


@pytest.mark.mobile
def test_swipe_complete_task_mobile(mobile_driver):
    driver = mobile_driver
    element = driver.find_element("xpath", "//android.widget.TextView[@text='Mobile task']")
    driver.swipe(start_x=element.location["x"], start_y=element.location["y"], end_x=element.location["x"] - 600,
                 end_y=element.location["y"])
    assert not driver.find_elements("xpath", "//android.widget.TextView[@text='Mobile task']")
