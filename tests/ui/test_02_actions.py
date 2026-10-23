import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_fill_clear_and_press_sequentially(lab):
    name = lab.get_by_label("Full name", exact=True)
    name.fill("Old value")
    name.clear()
    name.press_sequentially("Archana")  # Use only when per-key events matter; fill is faster.
    expect(name).to_have_value("Archana")
    name.press("ControlOrMeta+A")
    name.press("Backspace")
    expect(name).to_be_empty()


def test_textarea_and_contenteditable(lab):
    lab.get_by_label("Biography").fill("Python\nPlaywright")
    expect(lab.get_by_label("Biography")).to_have_value("Python\nPlaywright")
    lab.get_by_role("textbox", name="Notes").fill("API and UI")
    expect(lab.get_by_role("textbox", name="Notes")).to_have_text("API and UI")


def test_checkbox_radio_and_set_checked(lab):
    terms = lab.get_by_role("checkbox", name="Accept terms")
    terms.check()
    expect(terms).to_be_checked()
    terms.uncheck()
    expect(terms).not_to_be_checked()
    terms.set_checked(True)
    lab.get_by_role("radio", name="Premium", exact=True).check()
    expect(lab.get_by_role("radio", name="Premium", exact=True)).to_be_checked()


def test_select_single_and_multiple(lab):
    country = lab.get_by_label("Country", exact=True)
    country.select_option(label="United States")
    expect(country).to_have_value("us")
    country.select_option("in")
    expect(country).to_have_value("in")
    lab.get_by_label("Skills").select_option(["python", "api"])
    expect(lab.get_by_label("Skills")).to_have_values(["python", "api"])


def test_double_and_right_click(lab):
    lab.locator("#double").dblclick()
    expect(lab.locator("#double")).to_have_text("Double clicked")
    lab.locator("#right").click(button="right")
    expect(lab.locator("#right")).to_have_text("Right clicked")


def test_hover_and_focus(lab):
    lab.locator("#hover-zone").hover()
    expect(lab.locator("#hover-note")).to_be_visible()
    name = lab.get_by_label("Full name", exact=True)
    name.focus()
    expect(name).to_be_focused()
    name.blur()
    expect(name).not_to_be_focused()


def test_drag_and_drop(lab):
    lab.locator("#drag").drag_to(lab.locator("#drop"))
    expect(lab.locator("#drop")).to_have_text("Payment dropped")


def test_keyboard_and_mouse_low_level(lab):
    name = lab.get_by_label("Full name", exact=True)
    name.click()
    lab.keyboard.insert_text("Keyboard input")
    expect(name).to_have_value("Keyboard input")
    lab.locator("#double").scroll_into_view_if_needed()
    box = lab.locator("#double").bounding_box()
    assert box is not None
    lab.mouse.dblclick(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
    expect(lab.locator("#double")).to_have_text("Double clicked")
    lab.mouse.wheel(0, 200)


def test_dispatch_event_is_synthetic(lab):
    # dispatch_event does NOT prove a real user could interact. Prefer click for user flows.
    lab.locator("#save").dispatch_event("click")
    expect(lab.locator("#saved")).to_have_text("Saved")
