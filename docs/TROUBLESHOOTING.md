# Troubleshooting

| Symptom | Fix |
| --- | --- |
| No module named playwright/pytest | Use the `.venv` Python for installation and test execution; select it in the editor |
| Browser executable does not exist | Run `python -m playwright install chromium` with that same interpreter |
| Browser download fails | Check network/proxy/firewall and official Playwright installation guidance; retry on a normal network |
| Linux missing shared libraries | Install the official browser host dependencies through your system's approved package setup |
| Editor discovers no tests | Open the project root; select `.venv`; enable pytest; inspect Testing output |
| pytest cannot import pages/demo_app | Run from the root containing pyproject.toml; its pythonpath setting includes this folder |
| Strict mode violation | Narrow by semantic name or container; do not silence it with arbitrary nth() |
| Timeout on a visible element | Check wrong frame/tab, duplicate match, disabled state, obstruction, or app readiness in the trace |
| Unexpected 401 | Separate API contexts do not inherit browser cookies; log in or transfer state explicitly |
| A dialog stalls | A registered handler must accept or dismiss it |
| Manual app says port in use | Stop the previous manual app; automated tests select an available port independently |
| PDF fails in headed mode | Run the PDF test headless; it skips automatically in headed mode |
| HAR misses a request | Check URL/method/body mismatch, service workers and recording completeness |
| PowerShell blocks activation | Use `.\.venv\Scripts\python.exe` directly; activation is optional |

Use `python -m pytest --collect-only -q` to inspect discovery. API-only tests do not
need an installed browser. Browser tests require downloaded binaries and suitable OS
libraries. No tests were run on the user's Windows machine; see VALIDATION.md for the
author's environment and commands.
