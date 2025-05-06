import os
import requests


class TaskApi:
    base_url = "https://api.todoist.com/api/v1"
    token = os.getenv("TODOIST_TOKEN", "your_token_here")
    headers = {"Authorization": f"Bearer {token}"}

    def create_task(self, task_data):
        return requests.post(
            f"{self.base_url}/tasks", json=task_data, headers=self.headers
        )

    def get_task(self, task_id):
        return requests.get(f"{self.base_url}/tasks/{task_id}", headers=self.headers)

    def delete_task(self, task_id):
        return requests.delete(f"{self.base_url}/tasks/{task_id}", headers=self.headers)
