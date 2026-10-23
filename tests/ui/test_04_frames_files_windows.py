import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


def test_iframe_with_frame_locator(lab):
    field = lab.frame_locator('iframe[title="Payment details"]').get_by_label("Card number")
    field.fill("4242424242424242")
    expect(field).to_have_value("4242424242424242")


def test_open_shadow_root(lab):
    # Playwright locators pierce OPEN shadow roots. XPath does not.
    lab.get_by_label("Shadow input").fill("Shadow value")
    expect(lab.locator("practice-widget").get_by_role("textbox")).to_have_value("Shadow value")


def test_popup_register_listener_before_action(lab):
    with lab.expect_popup() as popup_info:
        lab.get_by_role("link", name="Open payment tab").click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    expect(popup.get_by_label("Card number")).to_be_visible()
    popup.close()


def test_context_new_page_and_page_event(context, lab, base_url):
    with context.expect_page() as info:
        lab.get_by_role("link", name="Open payment tab").click()
    new_tab = info.value
    expect(new_tab).to_have_url(base_url + "/frame")
    new_tab.close()
    manual_tab = context.new_page()
    manual_tab.goto(base_url)
    expect(manual_tab).to_have_title("PayFlow Practice")
    manual_tab.close()


def test_upload_disk_file_and_clear(lab, tmp_path):
    document = tmp_path / "notes.txt"
    document.write_text("Playwright practice", encoding="utf-8")
    field = lab.get_by_label("Upload document")
    field.set_input_files(document)
    expect(lab.locator("#upload-result")).to_have_text("notes.txt")
    field.set_input_files([])
    expect(lab.locator("#upload-result")).to_be_empty()


def test_upload_multiple_memory_files(lab):
    lab.get_by_label("Upload document").set_input_files(
        [
            {"name": "one.txt", "mimeType": "text/plain", "buffer": b"one"},
            {"name": "two.txt", "mimeType": "text/plain", "buffer": b"two"},
        ]
    )
    expect(lab.locator("#upload-result")).to_have_text("one.txt, two.txt")


def test_file_chooser(lab):
    with lab.expect_file_chooser() as chooser:
        lab.get_by_role("button", name="Choose file").click()
    chooser.value.set_files({"name": "chosen.txt", "mimeType": "text/plain", "buffer": b"hello"})
    expect(lab.locator("#upload-result")).to_have_text("chosen.txt")


def test_download_and_verify_content(lab, tmp_path):
    with lab.expect_download() as download_info:
        lab.get_by_role("link", name="Download payments").click()
    download = download_info.value
    assert download.suggested_filename == "payments.csv"
    target = tmp_path / download.suggested_filename
    download.save_as(target)
    assert download.failure() is None
    assert "Practice transfer,100" in target.read_text(encoding="utf-8")


def test_navigation_history(page, base_url):
    page.goto(base_url)
    page.get_by_role("link", name="UI operations lab").click()
    expect(page).to_have_url(base_url + "/lab")
    page.go_back()
    expect(page).to_have_title("PayFlow Practice")
    page.go_forward()
    page.reload()
    expect(page).to_have_title("UI Operations Lab")
