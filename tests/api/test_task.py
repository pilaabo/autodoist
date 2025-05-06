import pytest
from api.models.task_create import TaskCreate


@pytest.mark.parametrize(
    "created_task,expected_content",
    [
        ({"content": "Simple task"}, "Simple task"),
        ({"content": "Another task"}, "Another task"),
    ],
    indirect=["created_task"],
)
def test_task_creation(created_task, expected_content):
    assert created_task["content"] == expected_content
