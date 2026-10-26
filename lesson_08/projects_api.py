import requests
from config import TOKEN, BASE_URL


class ProjectsAPI:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
        self.url = f"{BASE_URL}/projects"

    def create_project(self, title):
        return requests.post(
            self.url,
            json={"title": title},
            headers=self.headers
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.url}/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.url}/{project_id}",
            json={"title": title},
            headers=self.headers
        )

    def delete_project(self, project_id):
        return requests.delete(
            f"{self.url}/{project_id}",
            headers=self.headers
        )
