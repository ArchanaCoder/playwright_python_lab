# Playwright Python Lab — UI + API

A runnable learning project for Archana: Python, pytest, Playwright, Page Objects,
API clients, and a local payment-themed practice application. No public demo site,
external account, paid service, database, or JavaScript build setup is needed.

**Start here → install → run one test → inspect the test → change it yourself.**

## What “all operations” means here

This project interprets your request as **Playwright's Python UI and HTTP API operations**,
not every operation in Python's standard library. It contains a broad runnable training
suite and a complete automatically generated **public SDK class/member index
for the pinned version** in [docs/API_CATALOG.md](docs/API_CATALOG.md).

It does **not** claim executable coverage of every method, every parameter combination,
every browser, or every future documentation addition. Remote browser connections,
extensions, client certificates, proxy infrastructure, experimental features and legacy
ElementHandle APIs need different setups; these are explicitly listed in
[docs/COVERAGE.md](docs/COVERAGE.md). No placeholder tests pretend to cover these.

## 1. Open the folder

Extract the ZIP, then open the **playwright_python_lab** folder containing this README.

- **Visual Studio Code:** File → Open Folder. Install the recommended Python and Ruff
  extensions. Run **Python: Select Interpreter** and select the `.venv` interpreter.
- **Visual Studio 2022:** Install the **Python development** workload, then File → Open →
  Folder. Use the integrated terminal and the commands below. The `.vscode` debugging
  configurations apply to VS Code; this is a Python folder project, not a .NET solution.

## 2. Install — Windows PowerShell

Python 3.11+ is required; this project was tested with Python 3.12.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m playwright install chromium
.\.venv\Scripts\python.exe -m pytest tests/ui/test_01_locators.py --headed -v
```

These commands do not require activating PowerShell scripts or changing execution policy.
Use `.\.venv\Scripts\python.exe` instead of `python` in later commands if the virtual
environment is not activated.

macOS / Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python -m pytest tests/ui/test_01_locators.py --headed -v
```

Linux hosts may also require `python -m playwright install-deps chromium` with their
normal system administrator permissions. Browser downloads need internet access once;
tests subsequently use only the local server.

## 3. Run and explore

All commands below assume your selected terminal Python is the virtual environment.
The fixture starts/stops the app automatically on an available port.

```bash
python -m pytest                                      # complete Chromium suite
python -m pytest tests/ui --headed --slowmo 150 -v     # watch UI operations
python -m pytest tests/api -v                         # API only; no browser install needed
python -m pytest tests/integration -v                 # realistic UI + API workflows
python -m pytest tests/advanced -v                    # context/network/device examples
python -m pytest -n 2                                 # parallel workers, isolated app per worker
python -m pytest --html=artifacts/report.html --self-contained-html
python -m pytest tests/ui/test_02_actions.py -k checkbox -v
python -m ruff check .
python -m ruff format --check .
```

For other browsers:

```bash
python -m playwright install firefox webkit
python -m pytest --browser firefox
python -m pytest --browser webkit
```

Chromium-only examples skip explicitly on other browsers. PDF requires headless mode:
the PDF test skips automatically in headed mode.
See [docs/VALIDATION.md](docs/VALIDATION.md) for what was actually verified here.

## 4. Try the app manually

```bash
python -m demo_app.app
```

Open http://127.0.0.1:8765 and http://127.0.0.1:8765/lab.
Practice credentials: **archana / practice123**. These are public dummy credentials
for this local teaching app. All data is in memory and resets when the server stops.
The demo authentication is intentionally minimal and not a production auth design.

## 5. Debug in your editor

- VS Code Testing panel: discover tests, then click Run Test / Debug Test.
- Open a test file and choose **Debug current test file** from Run and Debug.
- Add a breakpoint and inspect `page`, locators, response JSON, and fixture state.
- Use `page.pause()` temporarily for the Playwright Inspector; do not commit it.
- A Playwright failure retains a trace and screenshot under `artifacts/test-results/`.

```bash
python -m playwright show-trace path/to/trace.zip
python -m playwright codegen http://127.0.0.1:8765/lab
```

Start the app manually before codegen. For the standalone asynchronous example, run
`python -m examples.async_example` in a second terminal (or add `--browser firefox`). Use recorded output as a starting point;
replace fragile locators, add expectations, and remove generated duplication.
The Python pytest plugin runs these tests; there is no Java-style runner class.

## Folder guide

| Folder/file | Purpose |
| --- | --- |
| `demo_app/` | Local Flask app, UI operations playground, in-memory REST API |
| `pages/` | UI page objects with reusable actions and locators |
| `clients/` | Small API client; assertions stay visible in tests |
| `tests/conftest.py` | Free-port server, browser configuration, API fixtures, owned-data cleanup |
| `tests/ui/` | Focused, numbered UI examples |
| `tests/api/` | HTTP methods, payloads, auth, status codes, CRUD, contracts |
| `tests/integration/` | UI + API business workflows |
| `tests/advanced/` | Contexts, auth state, HAR, workers, clock, WebSockets, CDP |
| `examples/` | Standalone async Playwright example |
| `docs/` | Coverage map, full SDK index, study plan, best practices, troubleshooting |
| `.vscode/` | Python test discovery, debug configurations, tasks, extension recommendations |
| `.github/workflows/` | Example CI pipeline |
| `artifacts/` | Generated reports and diagnostics; ignored by Git |

## Recommended reading order

1. [docs/LEARNING_PATH.md](docs/LEARNING_PATH.md)
2. `tests/ui/test_01_locators.py` → `test_06_network.py`
3. `tests/api/test_01_http_operations.py` → `test_02_auth_crud_contracts.py`
4. `tests/integration/test_payment_workflows.py`
5. [docs/BEST_PRACTICES.md](docs/BEST_PRACTICES.md)
6. `tests/advanced/` and [docs/COVERAGE.md](docs/COVERAGE.md)
7. [docs/API_CATALOG.md](docs/API_CATALOG.md) for searching operations

Regenerate the catalog after an intentional dependency upgrade:

```bash
python scripts/generate_api_catalog.py
```

Do not blindly upgrade dependencies; rerun lint, collection, and the browser suite.

Official sources: [Python introduction](https://playwright.dev/python/docs/intro),
[locators](https://playwright.dev/python/docs/locators),
[actionability](https://playwright.dev/python/docs/actionability),
[pytest plugin](https://playwright.dev/python/docs/test-runners),
[API testing](https://playwright.dev/python/docs/api-testing),
[API reference](https://playwright.dev/python/docs/api/class-playwright).
