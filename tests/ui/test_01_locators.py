"""Stable semantic locators first; CSS examples show when a contract is needed."""

import re

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_role_label_placeholder_text_and_test_id(lab):
    field = lab.get_by_label("Full name", exact=True)
    field.fill("Archana")
    expect(lab.get_by_placeholder("Enter full name")).to_have_value("Archana")
    expect(lab.get_by_test_id("full-name")).to_have_value("Archana")
    expect(lab.get_by_title("Your full name", exact=True)).to_have_value("Archana")
    expect(lab.get_by_alt_text("Practice logo")).to_be_visible()
    lab.get_by_role("button", name="Save profile").click()
    expect(lab.get_by_text("Saved", exact=True)).to_be_visible()


def test_css_xpath_and_chaining(lab):
    # CSS is useful for explicit application IDs. Avoid fragile positional XPath.
    lab.locator("#full-name").fill("Python")
    expect(lab.locator('xpath=//input[@id="full-name"]')).to_have_value("Python")
    section = lab.locator("section").filter(
        has=lab.get_by_role("heading", name="Forms and locators")
    )
    expect(section.get_by_role("button", name="Save profile")).to_be_enabled()


def test_filter_has_has_text_and_regex(lab):
    row = lab.get_by_role("row").filter(has_text="Savings")
    expect(row.get_by_role("cell").last).to_have_text("1200")
    products = lab.get_by_role("list", name="Products")
    item = products.get_by_role("listitem").filter(has_text=re.compile("^Python"))
    expect(item.get_by_role("button", name="Add")).to_have_count(1)
    expect(products.get_by_role("listitem").filter(has_not_text="API")).to_have_count(2)


def test_list_order_count_and_snapshot_reads(lab):
    items = lab.get_by_role("list", name="Products").get_by_role("listitem")
    expect(items).to_have_count(3)  # Wait for readiness before immediate snapshot reads.
    expect(items.first).to_contain_text("Python")
    expect(items.nth(1)).to_contain_text("API")
    assert len(items.all()) == 3
    assert items.count() == 3
    assert "UI course" in items.all_text_contents()[2]
    assert "Python" in items.first.inner_text()
    assert "Python" in items.first.text_content()


def test_locator_and_or(lab):
    field = lab.get_by_label("Full name").and_(lab.get_by_placeholder("Enter full name"))
    expect(field).to_be_editable()
    # or_ can match BOTH alternatives; narrow it deliberately instead of hiding ambiguity.
    alternative = lab.get_by_text("No such message", exact=True).or_(lab.locator("#saved"))
    expect(alternative).to_have_count(1)
