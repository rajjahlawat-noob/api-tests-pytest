import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api():
    """Shared HTTP session with base URL + default timeout."""
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json; charset=UTF-8"})

    def call(method, path, **kw):
        kw.setdefault("timeout", 15)
        return s.request(method, BASE_URL + path, **kw)

    yield call
    s.close()
