import allure
import pytest
from api.task_api import TaskApi


@pytest.fixture
def task_payload():
    return {"content": "Simple task"}


@pytest.fixture
def created_task(task_api, task_payload):
    with allure.step("Create task"):
        response = task_api.create_task(task_payload)
        task = response.json()

    yield task

    with allure.step("Delete task"):
        task_api.delete_task(task["id"])


@pytest.fixture(scope="module")
def task_api():
    return TaskApi()
