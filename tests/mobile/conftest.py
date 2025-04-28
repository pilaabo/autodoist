import pytest
from appium import webdriver

@pytest.fixture(scope="session")
def mobile_driver():
    caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "appPackage": "com.todoist",
        "appActivity": "com.todoist.activity.Main",
        "automationName": "UiAutomator2",
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    yield driver
    driver.quit()