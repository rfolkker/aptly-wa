#!/usr/bin/python3
import requests

class API:
    base_url = ""
    api_token = False
    headers = {"Content-Type": "application/json"}

    def __init__(self, base_url, api_token=None):
        self.base_url = base_url
        self.api_token = api_token

        if api_token:
            self.headers["Authorization"] = f"Bearer {api_token}"

    def _post(self, endpoint, data=None):
        response = requests.post(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def _put(self, endpoint, data=None):
        response = requests.put(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
class repo(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class DB(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Config(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Misc(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Publish(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Repo(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

    def create(self, repo_name, comment=None):
        endpoint = f"{self.base_url}/repos"
        data = {"Name": repo_name, "Comment": comment}
        response = self._post(endpoint, data)
        return response

    def upload(self, repo_name, file_path):
        endpoint = f"{self.base_url}/repos/{repo_name}/file/{file_path}"
        response = self._post(endpoint)
        return response

    def publish(self, repo_name, distribution, component):
        endpoint = f"{self.base_url}/repos/{repo_name}/publish/{distribution}"
        data = {"Sources": [{"Component": component}]}
        response = self._post(endpoint, data)
        return response

class Serve(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Snapshot(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)

class Task(API):
    def __init__(self, base_url, api_token=None):
        super.__init__(base_url, api_token)
