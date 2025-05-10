import pytest
import allure


def test_create_task(task_api, task_payload):
    with allure.step("Create task"):
        response = task_api.create_task(task_payload)
        assert response.status_code == 200
        created_task = response.json()

    with allure.step("Fetch created task"):
        fetched_task = task_api.get_task(created_task["id"]).json()

    with allure.step("Assert task is created"):
        assert fetched_task == created_task

    with allure.step("Delete task"):
        task_api.delete_task(created_task["id"])


@pytest.mark.parametrize(
    "invalid_payload,expected_error",
    [
        pytest.param({"content": ""}, "Invalid argument value", id="empty_content"),
        pytest.param(
            {"description": "Task with no content"},
            "Required argument is missing",
            id="missing_content_field",
        ),
    ],
)
def test_create_task_validation_errors(task_api, invalid_payload, expected_error):
    with allure.step("Try to create task with invalid payload"):
        response = task_api.create_task(invalid_payload)
        body = response.json()

    with allure.step("Assert task is not created"):
        assert response.status_code == 400
        assert body["error"] == expected_error


def test_delete_task_marks_entity_as_deleted(task_api, created_task):
    task_id = created_task["id"]

    with allure.step("Delete task"):
        delete_response = task_api.delete_task(task_id)
        assert delete_response.status_code == 204

    with allure.step("Fetch deleted task"):
        get_response = task_api.get_task(task_id)
        body = get_response.json()

    with allure.step("Assert task is marked as deleted"):
        assert get_response.status_code == 200
        assert body["is_deleted"] is True


@pytest.mark.parametrize(
    "new_content",
    ["Updated task content"],
)
def test_update_task(task_api, created_task, new_content):
    task_id = created_task["id"]


    with allure.step("Update task"):
        update_response = task_api.update_task(task_id, {"content": new_content})
        assert update_response.status_code == 200

    with allure.step("Fetch updated task"):
        updated_task = task_api.get_task(task_id).json()

    with allure.step("Assert task is updated"):
        assert updated_task["content"] == new_content
