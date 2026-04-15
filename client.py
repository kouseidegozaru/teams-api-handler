import requests

class APIClient:
    def __init__(self, base_url: str, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint: str, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()