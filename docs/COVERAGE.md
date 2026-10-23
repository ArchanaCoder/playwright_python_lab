# Operation coverage and explicit boundaries

The runnable examples below are the project's teaching scope. API_CATALOG.md inventories
all public SDK wrapper classes/members in the pinned installation; an inventory entry
is NOT an executable coverage claim. One API may expose many options that are not all
exercised here. No mini project can honestly promise every possible API combination.

## Runnable coverage

| Area | Operations and concepts | Example location |
| --- | --- | --- |
| Locators | role, label, text, placeholder, title, alt text, test ID; CSS, XPath, chaining, regex, filter/has/has-not-text, and/or | `tests/ui/test_01_locators.py` |
| Collections | count, first/last/nth, all, text extraction, table row scoping | `tests/ui/test_01_locators.py` |
| Forms | fill, clear, sequential keys, textarea, contenteditable, checkbox, uncheck, set_checked, radio, single/multiple select | `tests/ui/test_02_actions.py` |
| Pointer/keyboard | click/right/double, hover, focus/blur, drag_to, keyboard, mouse, scroll, bounding_box, synthetic events | `tests/ui/test_02_actions.py` |
| Waiting | actionability, auto-retrying expect, explicit state wait, timeout exception, trial click | `tests/ui/test_03_waits_assertions.py` |
| Assertions | visible/hidden, attached, enabled/disabled, editable, checked, focused, count, text, value(s), attributes, CSS, URL/title, accessible name, ARIA snapshot | UI tests throughout |
| Frames/shadow DOM | frame_locator, open shadow root traversal | `tests/ui/test_04_frames_files_windows.py` |
| Tabs/navigation | popup, context page event, new_page, go_back/go_forward/reload/load state | `tests/ui/test_04_frames_files_windows.py` |
| Files | disk/in-memory/multiple uploads, clear upload, file chooser; download name/content/failure/save | `tests/ui/test_04_frames_files_windows.py` |
| Dialogs | alert, confirmation accept/dismiss, prompt input | `tests/ui/test_05_dialogs_events.py` |
| JS/events | console/pageerror events, evaluate, evaluate_handle, property handles, expose_function, init scripts | `tests/ui/test_05_dialogs_events.py` |
| HTTP interception | request/response events and metadata, route.fulfill/fetch/continue_/fallback/abort, page/context routing, unroute | `tests/ui/test_06_network.py` |
| HTTP verbs | GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS via fetch | `tests/api/test_01_http_operations.py` |
| Payloads | JSON, raw text/bytes, URL-encoded form, multipart file and fields | `tests/api/test_01_http_operations.py` |
| Request options | params, headers, timeout, max_redirects, max_retries, fail_on_status_code | `tests/api/test_01_http_operations.py` |
| Responses | expect.to_be_ok, ok/status/status_text/url, headers/headers_array, text/body/JSON, dispose | `tests/api/test_01_http_operations.py` |
| Auth | valid/invalid/form login, cookie auth, bearer header, logout, separate request contexts | `tests/api/test_02_auth_crud_contracts.py` |
| CRUD/contracts | create/read/PUT replace/PATCH/delete, path/query parameters, missing resource, negative payloads, small contract checks | `tests/api/test_02_auth_crud_contracts.py` |
| Combined workflow | UI login/create; API setup/UI assertion; UI deletion/API assertion; cookie sharing and in-memory auth reuse | `tests/integration/test_payment_workflows.py` |
| Context state | add/read/clear cookies; local/session storage; storage_state restore; two isolated contexts | `tests/advanced/test_browser_contexts.py` |
| Emulation | viewport, media color/reduced motion, locale, timezone, geolocation, permissions, offline | `tests/advanced/test_browser_contexts.py` |
| Diagnostics | screenshots (page/locator), trace lifecycle, video recording | `tests/advanced/test_browser_contexts.py` |
| Advanced network | HAR record/replay, WebSocket routing/messages | `tests/advanced/test_network_clock_workers.py` |
| Worker/time | worker event/evaluate/message, clock install/fast_forward | `tests/advanced/test_network_clock_workers.py` |
| Browser-specific | headless PDF, mobile device/touch, Chromium CDP session | `tests/advanced/test_network_clock_workers.py` |
| Python async API | async lifecycle, await, async assertions, request | `examples/async_example.py` (standalone) |
| Framework | fixtures, teardown, parametrization, page objects, API client, xdist, HTML/JUnit, trace diagnostics, CI | Project-wide |

## Reference-only / requires a different environment

These APIs remain searchable in API_CATALOG.md. They are not marked covered by a test:

| Capability | Why it is not in the local default suite | Official starting point |
| --- | --- | --- |
| Remote `connect`, `connect_over_cdp` | Requires a separately hosted browser endpoint and lifecycle/security choices | BrowserType reference |
| Persistent browser profiles, extensions | Needs separate profile/extension lifecycle; avoid using your personal browser profile | BrowserType / Chrome extensions guides |
| HTTP basic auth, client certificates, proxies | Needs an appropriately configured protected server, TLS material or proxy | API testing / network guides |
| Certificate failures and ignore_https_errors | Local demo is HTTP; no fake claim of TLS verification | APIRequest / BrowserContext |
| Service worker interception/cache | Different lifecycle and routing caveats; HAR example explicitly blocks workers during replay | Service workers / network |
| Browser downloads, cancelled downloads, directory upload | Core file examples run; OS/path/cancellation variants require dedicated scenarios | Download / Locator |
| Clipboard/camera/microphone permissions | Browser and host dependent; geolocation demonstrates grant/clear permission mechanics | BrowserContext |
| IndexedDB auth persistence and sessionStorage restore recipe | Storage state example covers cookies/localStorage; sessionStorage is explicitly excluded | Authentication guide |
| Screenshot golden-baseline comparison | Screenshots run, but this project does not claim a visual-regression baseline system | Screenshots guide |
| Full accessibility auditing | Accessible-name and ARIA assertions are present; no axe audit integration is claimed | Accessibility testing |
| Third-party OAuth/SSO/MFA, CAPTCHA | Requires a controlled test identity/service contract | Authentication guide |
| GraphQL, SOAP, SSE, real WebSocket backend | HTTP payload mechanics apply; dedicated protocol examples are not included | Network / API testing |
| Crash/close/race branches, exhaustive event overloads | Happy paths and selected failures run; destructive lifecycle branches need isolated fixtures | Page / BrowserContext |
| Overlay handlers, locator masks, advanced Clock methods | Catalog entries available; not every helper/option has an executable example | Page / Locator / Clock |
| Experimental and newly introduced classes | Catalog reflects installed SDK wrappers; future docs may add APIs | API reference |
| Legacy ElementHandle/selector convenience methods | Prefer Locator APIs with web-first assertions; do not learn deprecated APIs as best practice | ElementHandle / Locator |

Documentation changes over time. The pinned SDK is the reproducible baseline. Check
an individual member's official documentation for added-version notes and browser support.
