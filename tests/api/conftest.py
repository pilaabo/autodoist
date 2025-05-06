import pytest
from api.task_api import TaskApi
from api.models.task_create import TaskCreate


@pytest.fixture()
def created_task(request):
    api = TaskApi()
    task_data = TaskCreate(**request.param)
    response = api.create_task(task_data.model_dump())
    task = response.json()
    yield task
    api.delete_task(task["id"])
