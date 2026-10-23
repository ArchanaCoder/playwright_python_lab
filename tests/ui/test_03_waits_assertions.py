import re

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_auto_wait_for_enabled_button(lab):
    lab.locator("#enable").click()
    lab.locator("#disabled").click()  # Waits for actionability; no time.sleep.
    expect(lab.locator("#disabled")).to_have_text("Executed")


def test_web_first_assertion_retries(lab):
    lab.locator("#load").click()
    expect(lab.locator("#delayed")).to_be_visible()
    expect(lab.locator("#delayed")).to_have_text("Result ready")


def test_explicit_state_wait(lab):
    lab.locator("#load").click()
    lab.locator("#delayed").wait_for(state="visible")
    expect(lab.locator("#delayed")).to_be_attached()


def test_page_attribute_css_and_accessibility_assertions(lab):
    expect(lab).to_have_title("UI Operations Lab")
    expect(lab).to_have_url(re.compile(r"/lab$"))
    field = lab.get_by_label("Full name", exact=True)
    expect(field).to_have_attribute("placeholder", "Enter full name")
    expect(field).to_have_id("full-name")
    expect(field).to_have_accessible_name("Full name")
    expect(lab.locator("#delayed")).to_be_hidden()
    expect(lab.locator("#disabled")).to_be_disabled()
    expect(lab.locator("body")).to_have_css("display", "block")
    expect(lab.get_by_role("list", name="Products")).to_match_aria_snapshot(
        '- list "Products":\n  - listitem:\n    - text: Python course\n    - button "Add"\n  - listitem:\n    - text: API course\n    - button "Add"\n  - listitem:\n    - text: UI course\n    - button "Add"'
    )


def test_timeout_is_observable_and_bounded(lab):
    with pytest.raises(PlaywrightTimeoutError):
        lab.get_by_role("button", name="Does not exist", exact=True).click(timeout=200)


def test_trial_action_checks_without_clicking(lab):
    lab.locator("#save").click(trial=True)
    expect(lab.locator("#saved")).to_be_empty()
