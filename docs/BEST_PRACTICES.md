# Best practices illustrated in this project

1. **Test behaviour.** Click a named button and assert a user-visible result. Avoid
   treating a successful click or HTTP 200 as proof of business correctness.
2. **Prefer role/label/test-ID contracts.** Use exact names and container scoping.
   Use CSS for stable IDs where appropriate. Avoid deeply nested positional XPath.
3. **Understand strictness.** A single-element action should resolve uniquely.
   Do not add `.first` blindly to conceal an ambiguous locator.
4. **Trust actionability, then assert outcomes.** A click waits for relevant action
   checks; it does not know your business workflow finished. Use `expect` or a specific
   response/event. Avoid fixed sleeps and generic `networkidle` readiness checks.
5. **Snapshot reads are immediate.** `all()`, `count()`, `is_visible()` and text reads
   are useful observations but do not replace auto-retrying assertions.
6. **Own test state.** New context per test; generated resource IDs; fixture teardown;
   no test-order dependencies. Each parallel worker has its own app and available port.
7. **Register event waits before actions.** `with page.expect_download(): click()`
   prevents missing a fast download. The same applies to popups and responses.
8. **Keep page objects small.** UI mechanics belong in page objects; expectations
   stay visible in tests. Avoid one massive BasePage wrapping every Playwright method.
9. **Keep API clients thin.** Return APIResponse; tests assert status, schema and
   business values. Separate setup from assertions where the scenario benefits.
10. **Share cookies deliberately.** `page.request` / `context.request` share browser
    cookies; `playwright.request.new_context()` is independent. Use storage state
    explicitly when moving authenticated sessions between contexts.
11. **Protect actual auth state.** Never commit tokens, .env files or storage_state.
    Here credentials are dummy values for a local-only training service.
12. **Close what you create.** Dispose request contexts, browser contexts and JS
    handles. Context closure flushes video/HAR. Plugin-managed fixtures clean themselves.
13. **Distinguish network mocking from integration.** Route fulfillment isolates UI
    behaviour; an API-to-UI workflow checks real local integration. Keep both.
14. **Inspect failures.** Review call log, trace, screenshot, console and request/response
    details. Do not fix a failure by increasing every timeout or enabling force=True.
15. **Use retries intentionally.** Transport max_retries is not HTTP-status retry logic.
    Keep flaky test investigation visible; this suite does not auto-rerun failed tests.
16. **Keep sync and async separate.** This pytest suite is synchronous. A standalone
    async example demonstrates `await`; do not nest sync Playwright in an event loop.
17. **Use appropriate assertions.** `expect(locator).to_have_text(...)` retries. A Python
    `assert response.json()[...]` is appropriate after an HTTP response is complete.
18. **Do not overengineer learning code.** No custom runner class, hidden global driver,
    environment-dependent public demo site, or wrapper for every SDK operation.

The local server intentionally has simple auth and in-memory storage. It is a test
fixture, not a reference architecture for a banking backend. Negative numeric/business
validation and realistic multi-user authorization are exercises, not claimed coverage.
