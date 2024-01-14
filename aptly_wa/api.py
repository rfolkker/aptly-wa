#!/usr/bin/python3
import requests
import shutil
from pprint import pprint
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

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
    
    def _get(self, endpoint, data=None):
        # TODO: Add step to convert data to parameters added to endpoint
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def _get_file(self, endpoint, filename):
        # TODO: Add step to convert data to parameters added to endpoint
        response = None
        return_value = filename
        try:
            response = requests.get(endpoint, headers=self.headers, stream=True)
            with open(filename, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        except:
            del response
            return_value = "" # Empty if we fail to save

        return return_value # Not session safe

    def _put(self, endpoint, data=None):
        response = requests.put(endpoint, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
class DB(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)

class Config(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)

class Misc(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)
    def graph(self):
        endpoint = f"{self.base_url}/graph.png"
        response = self._get_file(endpoint,"graph.png")
        return response
    def version(self):
        endpoint = f"{self.base_url}/version"
        response = self._get(endpoint )
        return response
    def healthy(self):
        # currently not enabled on server
        # endpoint = f"{self.base_url}/healthy"
        # response = self._get(endpoint )
        # return response
        return {"Status":"Feature not enabled"}
    def ready(self):
        # endpoint = f"{self.base_url}/ready"
        # response = self._get(endpoint )
        # return response
        return {"Status":"Feature not enabled"}

class Publish(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)

class Repo(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)

    def create(self, repo_name, comment=None):
        endpoint = f"{self.base_url}/repos"
        data = {"Name": repo_name, "Comment": comment}
        response = self._post(endpoint, data)
        return response

    def list(self):
        endpoint = f"{self.base_url}/repos"
        response = self._get(endpoint)
        return response
    # This should be added to the file package
    def assign_file(self, repo_name, file_path, file_data):
        endpoint = f"{self.base_url}/repos/{repo_name}/files/{file_path}"
        response = self._post(endpoint, file_data)
        return response

    def publish(self, repo_name, distribution, component):
        endpoint = f"{self.base_url}/repos/{repo_name}/publish/{distribution}"
        data = {"Sources": [{"Component": component}]}
        response = self._post(endpoint, data)
        return response

class Package(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)
    def list(self, repo_name):
        endpoint = f"{self.base_url}/repos/{repo_name}/packages"
        response = self._get(endpoint )
        return response

    def get(self, repo_name, package_name):
        endpoint = f"{self.base_url}/repos/{repo_name}/packages?q={package_name}&format=details"
        response = self._get(endpoint )
        return response

class Snapshot(API):
    def __init__(self, base_url, api_token=None):
        super().__init__(base_url, api_token)

def test_misc(api_url):
    misc = Misc(api_url)
    saved_file = misc.graph()
    print(f"Graph saved as [{saved_file}]")
    print("\nVersion")
    pprint(misc.version())
    print("\nHealth:")
    pprint(misc.healthy())
    print("\nReady:")
    pprint(misc.ready())

def test_packages(api_url):
    package = Package(api_url)
    print("Getting Packages:")
    print("Foo Repo:")
    pprint(package.list("foo"))
    print("\nWebmin Package")
    pprint(package.get("foo","webmin"))

def test_repos(api_url):
    repo = Repo(api_url)
    print("Getting Repos:")
    pprint(repo.list())

def main():
    api_url = "API_URL"
    test_repos(api_url)
    test_packages(api_url)
    test_misc(api_url)

if __name__ == '__main__':
    main()