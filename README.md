# API Tests with Pytest

![API Tests](https://github.com/rajjahlawat-noob/api-tests-pytest/actions/workflows/api-tests.yml/badge.svg)

REST API test suite for [JSONPlaceholder](https://jsonplaceholder.typicode.com) using **Python, pytest, requests and JSON Schema**.

## What's covered
- **CRUD**: GET, POST, PUT, DELETE
- **Schema validation** with `jsonschema`
- **Data-driven tests** with `@pytest.mark.parametrize`
- **Negative test**: missing resource returns 404
- **Data integrity**: user → posts relationship
- **Performance check**: response time under 2s

CI runs on every push **and daily** as an API health check, publishing an HTML report.

## Run locally
```bash
pip install -r requirements.txt
pytest -v
pytest --html=report.html --self-contained-html   # HTML report
```
