"""Fixtures own lifecycle and cleanup. No shared test order or external app needed."""

import logging
from threading import Thread

import pytest
from playwright.sync_api import expect
from werkzeug.serving import make_server

from clients.payments_client import PaymentsClient
from demo_app.app import DEMO_USER, create_app


@pytest.fixture(scope="session")
def base_url():
    # Port 0 asks the OS for a free port. Each xdist worker gets its own app.
    server = make_server("127.0.0.1", 0, create_app(), threaded=True)
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 900},
        "locale": "en-IN",
        "timezone_id": "Asia/Kolkata",
        "reduced_motion": "reduce",
    }


@pytest.fixture(scope="session", autouse=True)
def assertion_timeout():
    expect.set_options(timeout=5000)


@pytest.fixture
def lab(page, base_url):
    page.goto(base_url + "/lab")
    return page


@pytest.fixture
def api(playwright, base_url):
    # A separate request context does NOT automatically share the browser's cookies.
    context = playwright.request.new_context(base_url=base_url, timeout=10000)
    yield context
    context.dispose()


@pytest.fixture
def authed_api(api):
    response = api.post("/api/login", data=DEMO_USER)
    expect(response).to_be_ok()
    return api


@pytest.fixture
def payments_client(authed_api):
    return PaymentsClient(authed_api)


@pytest.fixture
def make_payment(payments_client):
    created_ids = []

    def create(name="Practice payment", amount=100):
        response = payments_client.create(name, amount)
        assert response.status == 201
        item = response.json()
        created_ids.append(item["id"])
        return item

    yield create
    # Cleanup only resources owned by this test; deletion is idempotent for teardown.
    for item_id in created_ids:
        response = payments_client.delete(item_id)
        assert response.status in (204, 404)
