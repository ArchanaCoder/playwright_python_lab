from uuid import uuid4

import pytest
from playwright.sync_api import expect

from demo_app.app import DEMO_USER

pytestmark = pytest.mark.api


def test_unauthorized_request(api):
    assert api.get("/api/items").status == 401


@pytest.mark.parametrize(
    "username,password", [("wrong", "practice123"), ("archana", "wrong"), ("", "")]
)
def test_invalid_login(api, username, password):
    response = api.post("/api/login", data={"username": username, "password": password})
    assert response.status == 401
    assert response.json()["error"] == "Invalid credentials"


def test_cookie_auth_and_logout(authed_api):
    expect(authed_api.get("/api/me")).to_be_ok()
    assert any(cookie["name"] == "session" for cookie in authed_api.storage_state()["cookies"])
    authed_api.post("/api/logout")
    assert authed_api.get("/api/me").status == 401


def test_bearer_auth_in_separate_context(playwright, api, base_url):
    token = api.post("/api/login", data=DEMO_USER).json()["token"]
    bearer = playwright.request.new_context(
        base_url=base_url, extra_http_headers={"Authorization": f"Bearer {token}"}
    )
    try:
        assert bearer.get("/api/me").json()["username"] == "archana"
    finally:
        bearer.dispose()


def test_create_read_replace_patch_delete(authed_api, make_payment):
    item = make_payment(name="Original", amount=100)
    path = f"/api/items/{item['id']}"
    assert authed_api.get(path).json() == item
    # PUT replaces the resource; PATCH changes selected fields.
    replaced = authed_api.put(path, data={"name": "Replacement", "amount": 200})
    assert replaced.json() == {"id": item["id"], "name": "Replacement", "amount": 200}
    patched = authed_api.patch(path, data={"amount": 300})
    assert patched.json()["name"] == "Replacement"
    assert patched.json()["amount"] == 300
    assert authed_api.delete(path).status == 204
    assert authed_api.get(path).status == 404


def test_path_query_parameters_and_contract(authed_api, make_payment):
    unique = "Payment-" + uuid4().hex
    item = make_payment(name=unique, amount=250)
    response = authed_api.get("/api/items", params={"q": unique})
    expect(response).to_be_ok()
    payload = response.json()
    # Small contract checks without coupling to unrelated fields or ordering.
    assert isinstance(payload["items"], list)
    assert isinstance(payload["count"], int)
    assert payload["count"] == 1
    assert payload["items"][0] == item
    assert isinstance(item["id"], str)
    assert isinstance(item["amount"], (int, float))


@pytest.mark.parametrize("payload", [{}, {"name": ""}, {"name": " "}, {"name": 123}])
def test_invalid_create(authed_api, payload):
    response = authed_api.post("/api/items", data=payload)
    assert response.status == 422
    assert response.json()["error"] == "name is required"


def test_missing_resource(authed_api):
    assert authed_api.get("/api/items/nonexistent").status == 404


def test_form_login(api):
    response = api.post("/api/login", form=DEMO_USER)
    expect(response).to_be_ok()
    assert api.get("/api/me").status == 200
