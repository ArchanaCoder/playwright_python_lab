import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_request_and_response_metadata(lab):
    with lab.expect_request("**/api/echo?*") as request_info:
        with lab.expect_response("**/api/echo?*") as response_info:
            lab.locator("#fetch").click()
    request = request_info.value
    response = response_info.value
    assert request.method == "GET"
    assert request.resource_type == "fetch"
    assert response.status == 200
    assert response.json()["query"] == {"q": "browser"}
    assert response.request.url == request.url
    assert response.finished() is None


def test_route_fulfill_mock(lab):
    lab.route("**/api/echo?*", lambda route: route.fulfill(json={"source": "mock", "items": []}))
    lab.locator("#fetch").click()
    expect(lab.locator("#network-result")).to_contain_text('"source":"mock"')
    lab.unroute("**/api/echo?*")


def test_route_fetch_then_modify(lab):
    def modify(route):
        response = route.fetch()
        body = response.json()
        body["intercepted"] = True
        route.fulfill(response=response, json=body)

    lab.route("**/api/echo?*", modify)
    lab.locator("#fetch").click()
    expect(lab.locator("#network-result")).to_contain_text('"intercepted":true')


def test_route_continue_modify_headers(lab):
    def add_header(route):
        route.continue_(headers={**route.request.headers, "X-Learning": "intercepted"})

    lab.route("**/api/echo?*", add_header)
    lab.locator("#fetch").click()
    expect(lab.locator("#network-result")).to_contain_text('"custom_header":"intercepted"')


def test_route_abort_and_request_failure(lab):
    lab.route("**/api/echo?*", lambda route: route.abort("failed"))
    with lab.expect_event("requestfailed") as info:
        lab.locator("#fetch").click()
    assert info.value.failure
    expect(lab.locator("#network-result")).to_have_text("Network unavailable")


def test_context_route_and_fallback(context, lab):
    context.route("**/api/echo?*", lambda route: route.fulfill(json={"layer": "context"}))
    lab.route("**/api/echo?*", lambda route: route.fallback())
    lab.locator("#fetch").click()
    expect(lab.locator("#network-result")).to_contain_text('"layer":"context"')
