import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.advanced


def test_clock_controls_timer(lab):
    lab.clock.install()
    lab.locator("#timer").click()
    lab.clock.fast_forward(5000)
    expect(lab.locator("#timer-result")).to_have_text("Timer finished")


def test_web_worker(lab):
    with lab.expect_worker() as info:
        lab.evaluate("""() => {window.practiceWorker = new Worker(URL.createObjectURL(
            new Blob(['self.onmessage=e=>postMessage(e.data*2)'],{type:'text/javascript'})));}""")
    worker = info.value
    assert worker.evaluate("1 + 2") == 3
    assert (
        lab.evaluate("""() => new Promise(resolve => {
        practiceWorker.onmessage=e=>resolve(e.data);practiceWorker.postMessage(7);
    })""")
        == 14
    )
    lab.evaluate("practiceWorker.terminate()")


def test_websocket_routing_without_real_socket_server(lab):
    lab.route_web_socket(
        "**/practice-ws", lambda ws: ws.on_message(lambda message: ws.send("echo:" + message))
    )
    result = lab.evaluate("""() => new Promise((resolve,reject) => {
        const ws=new WebSocket(location.origin.replace('http','ws')+'/practice-ws');
        ws.onopen=()=>ws.send('hello');ws.onmessage=e=>{resolve(e.data);ws.close()};ws.onerror=reject;
    })""")
    assert result == "echo:hello"


def test_record_and_replay_har(browser, base_url, tmp_path):
    har = tmp_path / "requests.har"
    recording = browser.new_context(record_har_path=har, record_har_content="embed")
    try:
        page = recording.new_page()
        page.goto(base_url + "/lab")
        page.locator("#fetch").click()
        expect(page.locator("#network-result")).to_contain_text('"method":"GET"')
    finally:
        recording.close()  # Flush HAR before replay.
    replay = browser.new_context(service_workers="block")
    try:
        replay.route_from_har(har, not_found="abort")
        page = replay.new_page()
        page.goto(base_url + "/lab")
        page.locator("#fetch").click()
        expect(page.locator("#network-result")).to_contain_text('"method":"GET"')
    finally:
        replay.close()


@pytest.mark.chromium
def test_pdf_export(page, base_url, browser_name, pytestconfig):
    if browser_name != "chromium":
        pytest.skip("PDF export requires headless Chromium")
    if pytestconfig.getoption("headed"):
        pytest.skip("PDF export requires headless mode")
    page.goto(base_url)
    assert page.pdf(format="A4", print_background=True).startswith(b"%PDF")


@pytest.mark.chromium
def test_mobile_touch(playwright, browser, base_url, browser_name):
    if browser_name != "chromium":
        pytest.skip("This device example is validated on Chromium")
    context = browser.new_context(**playwright.devices["Pixel 7"])
    try:
        page = context.new_page()
        page.goto(base_url + "/lab")
        page.locator("#save").tap()
        expect(page.locator("#saved")).to_have_text("Saved")
    finally:
        context.close()


@pytest.mark.chromium
def test_cdp_session(browser, base_url, browser_name):
    if browser_name != "chromium":
        pytest.skip("CDP is Chromium-specific")
    context = browser.new_context()
    try:
        page = context.new_page()
        page.goto(base_url)
        session = context.new_cdp_session(page)
        try:
            session.send("Performance.enable")
            assert isinstance(session.send("Performance.getMetrics")["metrics"], list)
        finally:
            session.detach()
    finally:
        context.close()
