# Validation record

Verified in the build environment on 15 October 2026 with Python 3.12.14,
Playwright 1.64.0, pytest 9.1.1 and Firefox 157 (Playwright Firefox build 1555).
See requirements.txt for the other pinned dependencies.

| Check | Result |
| --- | --- |
| `python -m ruff check .` | Passed |
| `python -m ruff format --check .` | Passed |
| Python compilation of app, pages, clients, tests, examples, scripts | Passed |
| `python -m pytest --collect-only -q` | 101 cases discovered |
| `python -m pytest tests/api -q` | 38 passed |
| Full suite with `--browser firefox` | 98 passed, 3 Chromium-specific cases skipped; 110.66 seconds |
| Locators + API + integration tests with `--browser firefox -n 2` | 46 passed; 14.81 seconds |
| Standalone async example with Firefox against an isolated local server | Passed UI assertion and API health request |
| Full Chromium suite / PDF / mobile-touch / CDP | Not executed: browser distribution downloads failed in this environment |
| WebKit | Not executed: host dependencies unavailable |
| Windows/macOS execution, VS Code GUI, Visual Studio GUI, GitHub Actions hosted run | Not executed here; configuration and commands provided |

The full run includes real local browser interactions, uploads/downloads, drag/drop,
HAR record/replay, mocked WebSockets, worker messaging, clock control, video, tracing,
authentication, REST methods and end-to-end payment workflows. It does not prove every
public API member or every browser/OS combination is supported by this project.

The constrained Linux build container required environment-only Firefox sandbox
settings (`MOZ_DISABLE_CONTENT_SANDBOX=1` and `MOZ_DISABLE_RDD_SANDBOX=1`) to launch
pages. These settings are NOT embedded in project code or CI. Normal desktop setups
should use normal browser defaults. This was an environment accommodation, not a test
assertion bypass.

After the full run, the PDF example received a small guard to skip headed mode rather
than fail. The guard's Chromium path remains unverified along with the other
Chromium-specific paths. Final lint, compilation and discovery checks passed.

Generated browser binaries, installed dependencies, temporary auth state, traces,
videos, screenshots, and caches are excluded from the source archive. Test counts
refer to parametrized cases, not unique Python functions. Test duration is specific
to this build host and is not a performance benchmark.
