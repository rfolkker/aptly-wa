from aptly_wa import api
from pprint import pprint

def test_package_list(api_url):
    test_package = api.Package(api_url)
    pprint(test_package.run("list", {"action":"list","repo_name":"foo"}))

def main():
    api_url = "http://192.168.68.112:8080/api"
    test_package_list(api_url)

if __name__ == '__main__':
    main()