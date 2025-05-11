import os
import requests

from utils.attach import log_and_attach_request, log_and_attach_response


class TaskApi:
    BASE_URL = "https://api.todoist.com/api/v1"

    def __init__(self):
        token = os.getenv("TODOIST_TOKEN")
        if not token:
            raise EnvironmentError("TODOIST_TOKEN is not set in environment variables")
        self.headers = {"Authorization": f"Bearer {token}"}

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        log_and_attach_request(response.request)
        log_and_attach_response(response)
        return response

    def create_task(self, task_data):
        return self._request("post", "/tasks", json=task_data)

    def get_task(self, task_id):
        return self._request("get", f"/tasks/{task_id}")

    def delete_task(self, task_id):
        return self._request("delete", f"/tasks/{task_id}")

    def update_task(self, task_id, task_data):
        return self._request("post", f"/tasks/{task_id}", json=task_data)
