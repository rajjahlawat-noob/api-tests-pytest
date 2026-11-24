import pytest
from jsonschema import validate

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}


def test_get_all_posts(api):
    r = api("GET", "/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100


def test_get_single_post_matches_schema(api):
    r = api("GET", "/posts/1")
    assert r.status_code == 200
    validate(r.json(), POST_SCHEMA)
    assert r.json()["id"] == 1


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_filter_posts_by_user(api, user_id):
    r = api("GET", "/posts", params={"userId": user_id})
    assert r.status_code == 200
    posts = r.json()
    assert posts, "expected at least one post"
    assert all(p["userId"] == user_id for p in posts)


def test_create_post(api):
    payload = {"title": "QA rocks", "body": "API test", "userId": 1}
    r = api("POST", "/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_post(api):
    r = api("PUT", "/posts/1", json={"id": 1, "title": "updated", "body": "b", "userId": 1})
    assert r.status_code == 200
    assert r.json()["title"] == "updated"


def test_delete_post(api):
    r = api("DELETE", "/posts/1")
    assert r.status_code == 200


def test_missing_post_returns_404(api):
    r = api("GET", "/posts/99999")
    assert r.status_code == 404


def test_response_time_under_2s(api):
    r = api("GET", "/posts/1")
    assert r.elapsed.total_seconds() < 2
