import os
from uuid import uuid4

import pytest
import requests

API_BASE_URL = "https://api.todoist.com/rest/v2"
TEST_TOKEN = os.getenv("TEST_TOKEN")
HEADERS = {"Authorization": f"Bearer {TEST_TOKEN}"}


@pytest.mark.api
def test_register_user_success():
    response = requests.post(f"{API_BASE_URL}/auth/register", json={
        "email": f"{os.getenv('TEST_EMAIL')}_{uuid4()}@example.com",
        "password": f"{os.getenv('TEST_PASSWORD')}",
    })
    assert response.status_code == 201
    data = response.json()
    assert "user_id" in data


@pytest.mark.api
def test_login_success():
    creds = {"email": os.getenv("TEST_EMAIL"), "password": os.getenv("TEST_PASSWORD")}
    response = requests.post(f"{API_BASE_URL}/auth/login", json=creds)
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.api
def test_create_task_success():
    payload = {"content": "Sample task", "due_string": "today"}
    response = requests.post(f"{API_BASE_URL}/tasks", json=payload, headers=HEADERS)
    assert response.status_code == 200
    task_id = response.json()["id"]
    # follow‑up: убедимся, что задача действительно создана
    get_resp = requests.get(f"{API_BASE_URL}/tasks/{task_id}", headers=HEADERS)
    assert get_resp.status_code == 200


@pytest.mark.api
def test_update_task_unauthorized():
    task_id = "123456789"
    upd_resp = requests.post(
        f"{API_BASE_URL}/tasks/{task_id}",
        json={"content": "Hacked"}
    )
    assert upd_resp.status_code == 401


@pytest.mark.api
def test_delete_project_not_found():
    resp = requests.delete(f"{API_BASE_URL}/projects/999999999", headers=HEADERS)
    assert resp.status_code == 404
