import pytest


def test_create_task(task_api, task_payload):
    response = task_api.create_task(task_payload)
    assert response.status_code == 200
    created_task = response.json()

    fetched_task = task_api.get_task(created_task["id"]).json()

    assert fetched_task == created_task == {
        **created_task,
        "content": task_payload["content"],
    }

    task_api.delete_task(created_task["id"])


@pytest.mark.parametrize(
    "invalid_payload,expected_error",
    [
        pytest.param({"content": ""}, "Invalid argument value", id="empty_content"),
        pytest.param(
            {"description": "This is a test task"},
            "Required argument is missing",
            id="missing_content_field",
        ),
    ],
)
def test_create_task_validation_errors(task_api, invalid_payload, expected_error):
    response = task_api.create_task(invalid_payload)
    body = response.json()

    assert response.status_code == 400
    assert body["error"] == expected_error


def test_delete_task_marks_entity_as_deleted(task_api, created_task):
    task_id = created_task["id"]

    delete_response = task_api.delete_task(task_id)
    assert delete_response.status_code == 204

    get_response = task_api.get_task(task_id)
    body = get_response.json()

    assert get_response.status_code == 200
    assert body["is_deleted"] is True


@pytest.mark.parametrize(
    "new_content",
    ["Updated task content"],
)
def test_update_task(task_api, created_task, new_content):
    task_id = created_task["id"]

    update_response = task_api.update_task(task_id, {"content": new_content})
    assert update_response.status_code == 200

    updated_task = task_api.get_task(task_id).json()
    assert updated_task["content"] == new_content
