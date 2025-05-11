import allure
from dotenv import load_dotenv
import pytest
import json
from pathlib import Path
from api.task_api import TaskApi


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


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


SCHEMAS_DIR = (
    Path(__file__).resolve().parent.parent.parent / "resources" / "json_schemas"
)


def _load_schema(*parts):
    path = SCHEMAS_DIR.joinpath(*parts).with_suffix(".json")
    return json.loads(path.read_text(encoding="utf‑8"))


@pytest.fixture(scope="session")
def schema_factory():
    return _load_schema


@pytest.fixture(scope="session")
def create_task_request_schema(schema_factory):
    return schema_factory("create_task", "request")


@pytest.fixture(scope="session")
def create_task_response_schema(schema_factory):
    return schema_factory("create_task", "response")


@pytest.fixture(scope="session")
def update_task_request_schema(schema_factory):
    return schema_factory("update_task", "request")


@pytest.fixture(scope="session")
def update_task_response_schema(schema_factory):
    return schema_factory("update_task", "response")
