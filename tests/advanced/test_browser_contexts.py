import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.advanced


def test_cookie_operations(context, page, base_url):
    context.add_cookies([{"name": "learning", "value": "python", "url": base_url}])
    assert any(cookie["name"] == "learning" for cookie in context.cookies(base_url))
    page.goto(base_url)
    assert "learning=python" in page.evaluate("document.cookie")
    context.clear_cookies(name="learning")
    assert not any(cookie["name"] == "learning" for cookie in context.cookies())


def test_local_session_storage_and_restored_state(browser, page, base_url, tmp_path):
    page.goto(base_url)
    page.evaluate("localStorage.setItem('theme', 'dark'); sessionStorage.setItem('tab', 'one')")
    state = tmp_path / "state.json"
    page.context.storage_state(path=state)
    restored = browser.new_context(storage_state=state)
    try:
        tab = restored.new_page()
        tab.goto(base_url)
        assert tab.evaluate("localStorage.getItem('theme')") == "dark"
        # storage_state does not preserve sessionStorage.
        assert tab.evaluate("sessionStorage.getItem('tab')") is None
    finally:
        restored.close()


def test_two_contexts_are_isolated(browser, base_url):
    first, second = browser.new_context(), browser.new_context()
    try:
        first.add_cookies([{"name": "only-first", "value": "yes", "url": base_url}])
        assert first.cookies()
        assert second.cookies() == []
    finally:
        first.close()
        second.close()


def test_viewport_and_media_emulation(page, base_url):
    page.set_viewport_size({"width": 600, "height": 800})
    page.emulate_media(color_scheme="dark", reduced_motion="reduce")
    page.goto(base_url)
    assert page.viewport_size == {"width": 600, "height": 800}
    assert page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")
    assert page.evaluate("matchMedia('(prefers-reduced-motion: reduce)').matches")


def test_locale_timezone_and_device_options(browser, base_url):
    context = browser.new_context(
        locale="en-IN",
        timezone_id="Asia/Kolkata",
        viewport={"width": 390, "height": 844},
        device_scale_factor=2,
    )
    try:
        page = context.new_page()
        page.goto(base_url)
        assert page.evaluate("navigator.language") == "en-IN"
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone") in (
            "Asia/Kolkata",
            "Asia/Calcutta",
        )
    finally:
        context.close()


def test_geolocation_permission_and_updates(context, page, base_url):
    context.grant_permissions(["geolocation"], origin=base_url)
    context.set_geolocation({"latitude": 17.385, "longitude": 78.4867})
    page.goto(base_url)
    coordinates = page.evaluate("""() => new Promise((resolve,reject) =>
        navigator.geolocation.getCurrentPosition(p => resolve({lat:p.coords.latitude, lon:p.coords.longitude}), reject))""")
    assert coordinates["lat"] == pytest.approx(17.385)
    context.clear_permissions()


def test_offline_network(context, page, base_url):
    page.goto(base_url + "/lab")
    context.set_offline(True)
    try:
        page.locator("#fetch").click()
        expect(page.locator("#network-result")).to_have_text("Network unavailable")
    finally:
        context.set_offline(False)


def test_screenshot_bytes_and_locator_screenshot(page, base_url):
    page.goto(base_url + "/lab")
    assert page.screenshot(full_page=True, animations="disabled").startswith(b"\x89PNG")
    assert page.get_by_role("heading", name="UI Operations Lab").screenshot().startswith(b"\x89PNG")


def test_trace_lifecycle(browser, base_url, tmp_path):
    # Separate context avoids double-starting the pytest plugin's trace recorder.
    context = browser.new_context()
    try:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        page.goto(base_url)
        expect(page).to_have_title("PayFlow Practice")
        trace = tmp_path / "trace.zip"
        context.tracing.stop(path=trace)
        assert trace.stat().st_size > 0
    finally:
        context.close()


def test_video_recording(browser, base_url, tmp_path):
    context = browser.new_context(record_video_dir=tmp_path)
    page = context.new_page()
    page.goto(base_url)
    expect(page).to_have_title("PayFlow Practice")
    video = page.video
    context.close()  # Video must finish writing before inspecting or saving.
    assert video is not None
    assert video.path().is_file()
