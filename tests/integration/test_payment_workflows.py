"""Business examples: API setup, UI verification, and test-owned cleanup."""

from uuid import uuid4

import pytest
from playwright.sync_api import expect

from demo_app.app import DEMO_USER
from pages.login_page import LoginPage
from pages.payments_page import PaymentsPage

pytestmark = pytest.mark.integration


def test_login_and_create_payment(page, base_url):
    login = LoginPage(page).open(base_url)
    login.login(**DEMO_USER)
    expect(login.message).to_have_text("Welcome, archana")
    payments = PaymentsPage(page)
    name = "UI-" + uuid4().hex
    item_id = None
    try:
        with page.expect_response(
            lambda response: (
                response.url.endswith("/api/items") and response.request.method == "POST"
            )
        ) as info:
            payments.create(name, 450)
        response = info.value
        assert response.status == 201
        item_id = response.json()["id"]
        expect(payments.message).to_have_text("Payment created")
        expect(payments.row(name)).to_contain_text("450")
    finally:
        if item_id:
            # page.request shares browser cookies, so it can clean up UI-created data.
            assert page.request.delete(f"{base_url}/api/items/{item_id}").status == 204


def test_api_setup_then_ui_verification(browser, base_url, authed_api, make_payment):
    name = "API-" + uuid4().hex
    make_payment(name, 625)
    # Reuse auth in memory, never commit storage_state containing credentials.
    context = browser.new_context(storage_state=authed_api.storage_state())
    try:
        page = context.new_page()
        page.goto(base_url)
        expect(PaymentsPage(page).row(name)).to_contain_text("625")
    finally:
        context.close()


def test_ui_delete_verified_by_api(browser, base_url, authed_api, make_payment):
    item = make_payment("Delete-" + uuid4().hex)
    context = browser.new_context(storage_state=authed_api.storage_state())
    try:
        page = context.new_page()
        page.goto(base_url)
        row = PaymentsPage(page).row(item["name"])
        row.get_by_role("button", name="Delete", exact=True).click()
        expect(row).to_have_count(0)
        assert authed_api.get(f"/api/items/{item['id']}").status == 404
    finally:
        context.close()
