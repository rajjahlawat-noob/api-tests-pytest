import re


def test_users_have_valid_emails(api):
    r = api("GET", "/users")
    assert r.status_code == 200
    pattern = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    for u in r.json():
        assert pattern.match(u["email"]), f"bad email: {u['email']}"


def test_user_posts_relationship(api):
    """Every post returned for a user belongs to that user (data integrity)."""
    r = api("GET", "/users/3/posts")
    assert r.status_code == 200
    assert {p["userId"] for p in r.json()} == {3}
