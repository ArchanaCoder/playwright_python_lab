import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_alert(lab):
    messages = []

    def accept(dialog):
        messages.append((dialog.type, dialog.message))
        dialog.accept()

    lab.once("dialog", accept)
    lab.locator("#alert").click()
    assert messages == [("alert", "Practice alert")]


@pytest.mark.parametrize("accept, expected", [(True, "Accepted"), (False, "Cancelled")])
def test_confirmation(lab, accept, expected):
    # A registered dialog handler MUST accept/dismiss or the action will stall.
    lab.once("dialog", lambda dialog: dialog.accept() if accept else dialog.dismiss())
    lab.locator("#confirm").click()
    expect(lab.locator("#dialog-result")).to_have_text(expected)


def test_prompt(lab):
    lab.once("dialog", lambda dialog: dialog.accept("Archana"))
    lab.locator("#prompt").click()
    expect(lab.locator("#dialog-result")).to_have_text("Archana")


def test_console_event(lab):
    with lab.expect_console_message() as info:
        lab.locator("#console").click()
    assert info.value.type == "log"
    assert info.value.text == "practice log"


def test_page_error_event(lab):
    with lab.expect_event("pageerror") as info:
        lab.locator("#error").click()
    assert "Practice error" in info.value.message


def test_evaluate_and_js_handle(lab):
    assert lab.evaluate("() => document.title") == "UI Operations Lab"
    assert lab.locator("#full-name").evaluate("el => el.tagName") == "INPUT"
    handle = lab.evaluate_handle("() => ({language: 'Python', count: 3})")
    try:
        assert handle.get_property("language").json_value() == "Python"
        assert handle.evaluate("value => value.count") == 3
    finally:
        handle.dispose()


def test_expose_function_and_init_script(context, page, base_url):
    context.add_init_script("window.practiceSeed = 'repeatable'")
    page.expose_function("python_add", lambda a, b: a + b)
    page.goto(base_url + "/lab")
    assert page.evaluate("window.practiceSeed") == "repeatable"
    assert page.evaluate("async () => await window.python_add(2, 3)") == 5
