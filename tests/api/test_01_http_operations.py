"""All HTTP verb helpers plus generic fetch, payloads, headers, and query parameters."""

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.api


@pytest.mark.parametrize("verb", ["get", "post", "put", "patch", "delete", "head"])
def test_http_verbs(api, verb):
    response = getattr(api, verb)("/api/echo")
    expect(response).to_be_ok()
    if verb == "head":
        assert response.body() == b""
    else:
        assert response.json()["method"] == verb.upper()


def test_options_using_fetch(api):
    response = api.fetch("/api/echo", method="OPTIONS")
    assert response.json()["method"] == "OPTIONS"


def test_json_body_query_and_headers(api):
    response = api.post(
        "/api/echo",
        params={"q": "payments & API"},
        headers={"X-Learning": "python"},
        data={"amount": 100, "active": True},
    )
    body = response.json()
    assert body["query"] == {"q": "payments & API"}
    assert body["custom_header"] == "python"
    assert body["json"] == {"amount": 100, "active": True}


def test_urlencoded_form(api):
    response = api.post("/api/echo", form={"name": "Archana", "course": "Playwright"})
    assert response.json()["form"]["course"] == "Playwright"


def test_raw_text_and_binary_payload(api):
    response = api.post("/api/echo", data="plain payload", headers={"Content-Type": "text/plain"})
    assert response.json()["body"] == "plain payload"
    response = api.post("/api/echo", data=b"binary payload")
    assert response.json()["body"] == "binary payload"


def test_multipart_upload(api):
    response = api.post(
        "/api/upload",
        multipart={
            "description": "Practice upload",
            "file": {"name": "sample.txt", "mimeType": "text/plain", "buffer": b"hello"},
        },
    )
    expect(response).to_be_ok()
    assert response.json() == {
        "filename": "sample.txt",
        "size": 5,
        "description": "Practice upload",
    }


def test_response_inspection_and_dispose(api):
    response = api.get("/api/text")
    assert response.ok
    assert response.status == 200
    assert response.status_text == "OK"
    assert response.url.endswith("/api/text")
    assert response.headers["content-type"].startswith("text/plain")
    assert any(h["name"].lower() == "content-type" for h in response.headers_array)
    assert response.text() == "Playwright practice"
    assert response.body() == b"Playwright practice"
    response.dispose()  # Releases the stored body. Context teardown also disposes responses.


def test_redirect_following_and_disabling(api):
    followed = api.get("/api/redirect")
    assert followed.status == 200
    assert followed.url.endswith("/health")
    not_followed = api.get("/api/redirect", max_redirects=0)
    assert not_followed.status == 302
    assert not_followed.headers["location"] == "/health"


@pytest.mark.parametrize("status", [400, 401, 403, 404, 409, 422, 429, 500, 503])
def test_error_statuses_are_responses_by_default(api, status):
    response = api.get(f"/api/status/{status}")
    assert response.status == status
    assert not response.ok
    assert response.json()["status"] == status


def test_fail_on_status_code_is_opt_in(api):
    from playwright.sync_api import Error

    with pytest.raises(Error, match="404"):
        api.get("/api/status/404", fail_on_status_code=True)


def test_request_options_timeout_and_transport_retry(api):
    # max_retries applies to supported transport failures, NOT HTTP 500 responses.
    response = api.get("/health", timeout=5000, max_retries=1)
    expect(response).to_be_ok()
