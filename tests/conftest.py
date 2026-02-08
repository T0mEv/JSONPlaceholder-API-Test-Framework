import pytest
import os
import requests
import json

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client(base_url):
    class Client:
        def __init__(self, base):
            self.base = base
            self.session = requests.Session()
            self.timeout = 10

        def get(self, endpoint):
            return self.session.get(f"{self.base}{endpoint}", timeout=self.timeout)

        def post(self, endpoint, data):
            return self.session.post(f"{self.base}{endpoint}", json=data, timeout=self.timeout)

        def put(self, endpoint, data):
            return self.session.put(f"{self.base}{endpoint}", json=data, timeout=self.timeout)

        def patch(self, endpoint, data):
            return self.session.patch(f"{self.base}{endpoint}", json=data, timeout=self.timeout)

        def delete(self, endpoint):
            return self.session.delete(f"{self.base}{endpoint}", timeout=self.timeout)

    return Client(base_url)

@pytest.fixture
def load_schema():
    def _load(schema_name):
        root_dir = os.path.dirname(os.path.dirname(__file__))
        file_path = os.path.join(root_dir, "schemas", f"{schema_name}.json")

        with open(file_path, "r") as schema_file:
            return json.load(schema_file)

    return _load