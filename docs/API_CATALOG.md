# Public Python Playwright API catalog

Generated from installed Playwright **1.64.0**. 41 SDK wrapper classes; 732 public member entries (inherited entries may repeat).

Public SDK wrapper classes, methods (including inherited public methods), and properties.
Signatures come from the installed SDK, not a scraped documentation snapshot.
This inventories the reference surface; see COVERAGE.md for runnable examples.
Parameters and overload details: follow each official class link.
Python type aliases, event-name overloads and private internals are outside this index.
The catalog includes discouraged/legacy APIs for discoverability, not recommendation.

## APIRequest

[Official reference](https://playwright.dev/python/docs/api/class-apirequest)

- `new_context(self, *, base_url: Optional[str] = None, client_certificates: Optional[Sequence[playwright._impl._api_structures.ClientCertificate]] = None, extra_http_headers: Optional[Dict[str, str]] = None, fail_on_status_code: Optional[bool] = None, http_credentials: Union[playwright._impl._api_structures.HttpCredentials, Sequence[playwright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, proxy: Optional[playwright._impl._api_structures.ProxySettings] = None, storage_state: Union[str, pathlib.Path, playwright._impl._api_structures.StorageState, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, user_agent: Optional[str] = None) -> 'APIRequestContext'`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`

## APIRequestContext

[Official reference](https://playwright.dev/python/docs/api/class-apirequestcontext)

- `add_cookies(self, cookies: Sequence[playwright._impl._api_structures.SetCookieParam]) -> None`
- `clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None`
- `cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[playwright._impl._api_structures.Cookie]`
- `delete(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `dispose(self, *, reason: Optional[str] = None) -> None`
- `fetch(self, url_or_request: Union[str, ForwardRef('Request')], *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `get(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `head(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `patch(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `post(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `put(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, playwright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'`
- `remove_listener(self, event: Any, f: Any) -> None`
- `storage_state(self, *, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> playwright._impl._api_structures.StorageState`
- `tracing` — property

## APIResponse

[Official reference](https://playwright.dev/python/docs/api/class-apiresponse)

- `body(self) -> bytes`
- `dispose(self) -> None`
- `headers` — property
- `headers_array` — property
- `json(self) -> Any`
- `ok` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `security_details(self) -> Optional[playwright._impl._api_structures.SecurityDetails]`
- `server_addr(self) -> Optional[playwright._impl._api_structures.RemoteAddr]`
- `status` — property
- `status_text` — property
- `text(self) -> str`
- `timing` — property
- `url` — property

## APIResponseAssertions

[Official reference](https://playwright.dev/python/docs/api/class-apiresponseassertions)

- `not_to_be_ok(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `to_be_ok(self) -> None`

## Browser

[Official reference](https://playwright.dev/python/docs/api/class-browser)

- `bind(self, title: str, *, host: Optional[str] = None, port: Optional[int] = None, workspace_dir: Optional[str] = None) -> playwright._impl._api_structures.BrowserBindResult`
- `browser_type` — property
- `close(self, *, reason: Optional[str] = None) -> None`
- `contexts` — property
- `is_connected(self) -> bool`
- `new_browser_cdp_session(self) -> 'CDPSession'`
- `new_context(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[playwright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[playwright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[playwright._impl._api_structures.HttpCredentials, Sequence[playwright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[playwright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[playwright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[playwright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, playwright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[playwright._impl._api_structures.ViewportSize] = None) -> 'BrowserContext'`
- `new_page(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[playwright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[playwright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[playwright._impl._api_structures.HttpCredentials, Sequence[playwright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[playwright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[playwright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[playwright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, playwright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[playwright._impl._api_structures.ViewportSize] = None) -> 'Page'`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `start_tracing(self, *, categories: Optional[Sequence[str]] = None, page: Optional[ForwardRef('Page')] = None, path: Union[pathlib.Path, str, NoneType] = None, screenshots: Optional[bool] = None) -> None`
- `stop_tracing(self) -> bytes`
- `unbind(self) -> None`
- `version` — property

## BrowserContext

[Official reference](https://playwright.dev/python/docs/api/class-browsercontext)

- `add_cookies(self, cookies: Sequence[playwright._impl._api_structures.SetCookieParam]) -> None`
- `add_init_script(self, script: Optional[str] = None, *, path: Union[pathlib.Path, str, NoneType] = None) -> 'SyncContextManager'`
- `background_pages` — property
- `browser` — property
- `clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None`
- `clear_permissions(self) -> None`
- `clock` — property
- `close(self, *, reason: Optional[str] = None) -> None`
- `cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[playwright._impl._api_structures.Cookie]`
- `credentials` — property
- `debugger` — property
- `expect_console_message(self, predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]`
- `expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager`
- `expect_page(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Page')]`
- `expose_binding(self, name: str, callback: Callable) -> 'SyncContextManager'`
- `expose_function(self, name: str, callback: Callable) -> 'SyncContextManager'`
- `grant_permissions(self, permissions: Sequence[str], *, origin: Optional[str] = None) -> None`
- `is_closed(self) -> bool`
- `new_cdp_session(self, page: Union[ForwardRef('Page'), ForwardRef('Frame')]) -> 'CDPSession'`
- `new_page(self) -> 'Page'`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `pages` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `request` — property
- `route(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any]], *, times: Optional[int] = None) -> 'SyncContextManager'`
- `route_from_har(self, har: Union[str, pathlib.Path], *, not_found: Optional[Literal['abort', 'fallback']] = None, update: Optional[bool] = None, update_content: Optional[Literal['attach', 'embed']] = None, update_mode: Optional[Literal['full', 'minimal']] = None, url: Union[str, Pattern[str], NoneType] = None) -> None`
- `route_web_socket(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Callable[[ForwardRef('WebSocketRoute')], Any]) -> None`
- `service_workers` — property
- `set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `set_extra_http_headers(self, headers: Dict[str, str]) -> None`
- `set_geolocation(self, geolocation: Optional[playwright._impl._api_structures.Geolocation] = None) -> None`
- `set_offline(self, offline: bool) -> None`
- `set_storage_state(self, storage_state: Union[str, pathlib.Path, playwright._impl._api_structures.StorageState]) -> None`
- `storage_state(self, *, credentials: Optional[bool] = None, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> playwright._impl._api_structures.StorageState`
- `tracing` — property
- `unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None`
- `unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None`
- `wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any`

## BrowserType

[Official reference](https://playwright.dev/python/docs/api/class-browsertype)

- `connect(self, endpoint: str, *, expose_network: Optional[str] = None, headers: Optional[Dict[str, str]] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'`
- `connect_over_cdp(self, endpoint_url: str, *, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, headers: Optional[Dict[str, str]] = None, is_local: Optional[bool] = None, no_defaults: Optional[bool] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'`
- `executable_path` — property
- `launch(self, *, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, headless: Optional[bool] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, proxy: Optional[playwright._impl._api_structures.ProxySettings] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None) -> 'Browser'`
- `launch_persistent_context(self, user_data_dir: Union[str, pathlib.Path], *, accept_downloads: Optional[bool] = None, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, client_certificates: Optional[Sequence[playwright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, device_scale_factor: Optional[float] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, extra_http_headers: Optional[Dict[str, str]] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[playwright._impl._api_structures.Geolocation] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, has_touch: Optional[bool] = None, headless: Optional[bool] = None, http_credentials: Union[playwright._impl._api_structures.HttpCredentials, Sequence[playwright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[playwright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[playwright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[playwright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, slow_mo: Optional[float] = None, strict_selectors: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, timezone_id: Optional[str] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None, user_agent: Optional[str] = None, viewport: Optional[playwright._impl._api_structures.ViewportSize] = None) -> 'BrowserContext'`
- `name` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`

## CDPSession

[Official reference](https://playwright.dev/python/docs/api/class-cdpsession)

- `detach(self) -> None`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `send(self, method: str, params: Optional[Dict] = None) -> Dict`

## Clock

[Official reference](https://playwright.dev/python/docs/api/class-clock)

- `fast_forward(self, ticks: Union[int, str]) -> None`
- `install(self, *, time: Union[float, str, datetime.datetime, NoneType] = None) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `pause_at(self, time: Union[float, str, datetime.datetime]) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `resume(self) -> None`
- `run_for(self, ticks: Union[int, str]) -> None`
- `set_fixed_time(self, time: Union[float, str, datetime.datetime]) -> None`
- `set_system_time(self, time: Union[float, str, datetime.datetime]) -> None`

## ConsoleMessage

[Official reference](https://playwright.dev/python/docs/api/class-consolemessage)

- `args` — property
- `location` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `text` — property
- `timestamp` — property
- `type` — property
- `worker` — property

## Credentials

[Official reference](https://playwright.dev/python/docs/api/class-credentials)

- `create(self, rp_id: str, *, id: Optional[str] = None, private_key: Optional[str] = None, public_key: Optional[str] = None, sign_count: Optional[int] = None, user_handle: Optional[str] = None) -> playwright._impl._api_structures.VirtualCredential`
- `delete(self, id: str) -> None`
- `get(self, *, id: Optional[str] = None, rp_id: Optional[str] = None) -> List[playwright._impl._api_structures.VirtualCredential]`
- `install(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`

## Debugger

[Official reference](https://playwright.dev/python/docs/api/class-debugger)

- `next(self) -> None`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `paused_details` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `request_pause(self) -> None`
- `resume(self) -> None`
- `run_to(self, location: playwright._impl._api_structures.DebuggerLocation) -> None`

## Dialog

[Official reference](https://playwright.dev/python/docs/api/class-dialog)

- `accept(self, prompt_text: Optional[str] = None) -> None`
- `default_value` — property
- `dismiss(self) -> None`
- `message` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `type` — property

## Disposable

[Official reference](https://playwright.dev/python/docs/api/class-disposable)

- `close(self) -> None`
- `dispose(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`

## Download

[Official reference](https://playwright.dev/python/docs/api/class-download)

- `cancel(self) -> None`
- `delete(self) -> None`
- `failure(self) -> Optional[str]`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `path(self) -> pathlib.Path`
- `remove_listener(self, event: Any, f: Any) -> None`
- `save_as(self, path: Union[str, pathlib.Path]) -> None`
- `suggested_filename` — property
- `url` — property

## ElementHandle

[Official reference](https://playwright.dev/python/docs/api/class-elementhandle)

- `as_element(self) -> Optional[ForwardRef('ElementHandle')]`
- `bounding_box(self) -> Optional[playwright._impl._api_structures.FloatRect]`
- `check(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `content_frame(self) -> Optional[ForwardRef('Frame')]`
- `dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `dispatch_event(self, type: str, event_init: Optional[Dict] = None) -> None`
- `dispose(self) -> None`
- `eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any`
- `eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None) -> 'JSHandle'`
- `fill(self, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `focus(self) -> None`
- `get_attribute(self, name: str) -> Optional[str]`
- `get_properties(self) -> Dict[str, ForwardRef('JSHandle')]`
- `get_property(self, property_name: str) -> 'JSHandle'`
- `hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `inner_html(self) -> str`
- `inner_text(self) -> str`
- `input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `is_checked(self) -> bool`
- `is_disabled(self) -> bool`
- `is_editable(self) -> bool`
- `is_enabled(self) -> bool`
- `is_hidden(self) -> bool`
- `is_visible(self) -> bool`
- `json_value(self) -> Any`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `owner_frame(self) -> Optional[ForwardRef('Frame')]`
- `press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `query_selector(self, selector: str) -> Optional[ForwardRef('ElementHandle')]`
- `query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]`
- `remove_listener(self, event: Any, f: Any) -> None`
- `screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes`
- `scroll_into_view_if_needed(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `select_option(self, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]`
- `select_text(self, *, force: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `set_checked(self, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `set_input_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], playwright._impl._api_structures.FilePayload, Sequence[playwright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `tap(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `text_content(self) -> Optional[str]`
- `type(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `uncheck(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `wait_for_element_state(self, state: Literal['disabled', 'editable', 'enabled', 'hidden', 'stable', 'visible'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]`

## FileChooser

[Official reference](https://playwright.dev/python/docs/api/class-filechooser)

- `element` — property
- `is_multiple(self) -> bool`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `set_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], playwright._impl._api_structures.FilePayload, Sequence[playwright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`

## Frame

[Official reference](https://playwright.dev/python/docs/api/class-frame)

- `add_script_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, type: Optional[str] = None, url: Optional[str] = None) -> 'ElementHandle'`
- `add_style_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, url: Optional[str] = None) -> 'ElementHandle'`
- `check(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `child_frames` — property
- `click(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `content(self, *, include_shadow: Optional[bool] = None) -> str`
- `dblclick(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `dispatch_event(self, selector: str, type: str, event_init: Optional[Dict] = None, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `drag_and_drop(self, source: str, target: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[playwright._impl._api_structures.Position] = None, steps: Optional[int] = None, strict: Optional[bool] = None, target_position: Optional[playwright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None, *, strict: Optional[bool] = None) -> Any`
- `eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None) -> 'JSHandle'`
- `expect_navigation(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Response')]`
- `fill(self, selector: str, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `focus(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `frame_element(self) -> 'ElementHandle'`
- `frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'`
- `get_attribute(self, selector: str, name: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'`
- `get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'`
- `get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]`
- `hover(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `inner_html(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `inner_text(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `input_value(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `is_checked(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_detached(self) -> bool`
- `is_disabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_editable(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_enabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_hidden(self, selector: str, *, strict: Optional[bool] = None) -> bool`
- `is_visible(self, selector: str, *, strict: Optional[bool] = None) -> bool`
- `locator(self, selector: str, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'`
- `name` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `parent_frame` — property
- `press(self, selector: str, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `query_selector(self, selector: str, *, strict: Optional[bool] = None) -> Optional[ForwardRef('ElementHandle')]`
- `query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]`
- `remove_listener(self, event: Any, f: Any) -> None`
- `select_option(self, selector: str, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]`
- `set_checked(self, selector: str, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `set_content(self, html: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None`
- `set_input_files(self, selector: str, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], playwright._impl._api_structures.FilePayload, Sequence[playwright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `tap(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `text_content(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `title(self) -> str`
- `type(self, selector: str, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `uncheck(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `url` — property
- `wait_for_function(self, expression: str, *, arg: Optional[Any] = None, polling: Union[float, Literal['raf'], NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'`
- `wait_for_load_state(self, state: Optional[Literal['domcontentloaded', 'load', 'networkidle']] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]`
- `wait_for_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `wait_for_url(self, url: Union[str, Pattern[str], Callable[[str], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None`
- `webmcp` — property

## FrameLocator

[Official reference](https://playwright.dev/python/docs/api/class-framelocator)

- `first` — property
- `frame_locator(self, selector: str) -> 'FrameLocator'`
- `get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'`
- `get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'`
- `get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `last` — property
- `locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'`
- `nth(self, index: int) -> 'FrameLocator'`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `owner` — property
- `remove_listener(self, event: Any, f: Any) -> None`

## JSHandle

[Official reference](https://playwright.dev/python/docs/api/class-jshandle)

- `as_element(self) -> Optional[ForwardRef('ElementHandle')]`
- `dispose(self) -> None`
- `evaluate(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None) -> 'JSHandle'`
- `get_properties(self) -> Dict[str, ForwardRef('JSHandle')]`
- `get_property(self, property_name: str) -> 'JSHandle'`
- `json_value(self) -> Any`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`

## Keyboard

[Official reference](https://playwright.dev/python/docs/api/class-keyboard)

- `down(self, key: str) -> None`
- `insert_text(self, text: str) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `press(self, key: str, *, delay: Optional[float] = None) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `type(self, text: str, *, delay: Optional[float] = None) -> None`
- `up(self, key: str) -> None`

## Locator

[Official reference](https://playwright.dev/python/docs/api/class-locator)

- `all(self) -> List[ForwardRef('Locator')]`
- `all_inner_texts(self) -> List[str]`
- `all_text_contents(self) -> List[str]`
- `and_(self, locator: 'Locator') -> 'Locator'`
- `aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `blur(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `bounding_box(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[playwright._impl._api_structures.FloatRect]`
- `check(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `clear(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `content_frame` — property
- `count(self) -> int`
- `dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `describe(self, description: str) -> 'Locator'`
- `description` — property
- `dispatch_event(self, type: str, event_init: Optional[Dict] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `drag_to(self, target: 'Locator', *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[playwright._impl._api_structures.Position] = None, steps: Optional[int] = None, target_position: Optional[playwright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `drop(self, payload: playwright._impl._api_structures.DropPayload, *, position: Optional[playwright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `element_handle(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'ElementHandle'`
- `element_handles(self) -> List[ForwardRef('ElementHandle')]`
- `evaluate(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any`
- `evaluate_all(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'`
- `fill(self, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `filter(self, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None, visible: Optional[bool] = None) -> 'Locator'`
- `first` — property
- `focus(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `frame_locator(self, selector: str) -> 'FrameLocator'`
- `get_attribute(self, name: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'`
- `get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'`
- `get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `hide_highlight(self) -> None`
- `highlight(self, *, style: Optional[str] = None) -> None`
- `hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `inner_html(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `inner_text(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `is_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_editable(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_enabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `last` — property
- `locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'`
- `normalize(self) -> 'Locator'`
- `nth(self, index: int) -> 'Locator'`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `or_(self, locator: 'Locator') -> 'Locator'`
- `page` — property
- `press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `press_sequentially(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes`
- `scroll_into_view_if_needed(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `select_option(self, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]`
- `select_text(self, *, force: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `set_checked(self, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `set_input_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], playwright._impl._api_structures.FilePayload, Sequence[playwright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `tap(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `text_content(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `type(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `uncheck(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `visible` — property
- `wait_for(self, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `wait_for_function(self, expression: str, *, arg: Optional[Any] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `within(self, locator: 'Locator') -> 'Locator'`

## LocatorAssertions

[Official reference](https://playwright.dev/python/docs/api/class-locatorassertions)

- `not_to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None`
- `not_to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None`
- `not_to_have_accessible_description(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_css(self, name: str, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None`
- `not_to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_checked(self, *, checked: Optional[bool] = None, indeterminate: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None`
- `to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None`
- `to_have_accessible_description(self, description: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_css(self, name: str, value: Union[str, Pattern[str]], *, pseudo: Optional[Literal['after', 'before']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None`
- `to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`

## Mouse

[Official reference](https://playwright.dev/python/docs/api/class-mouse)

- `click(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None) -> None`
- `dblclick(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None) -> None`
- `down(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None`
- `move(self, x: float, y: float, *, steps: Optional[int] = None) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `up(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None`
- `wheel(self, delta_x: float, delta_y: float) -> None`

## Page

[Official reference](https://playwright.dev/python/docs/api/class-page)

- `add_init_script(self, script: Optional[str] = None, *, path: Union[pathlib.Path, str, NoneType] = None) -> 'SyncContextManager'`
- `add_locator_handler(self, locator: 'Locator', handler: Union[Callable[[ForwardRef('Locator')], Any], Callable[[], Any]], *, no_wait_after: Optional[bool] = None, times: Optional[int] = None) -> None`
- `add_script_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, type: Optional[str] = None, url: Optional[str] = None) -> 'ElementHandle'`
- `add_style_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, url: Optional[str] = None) -> 'ElementHandle'`
- `aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `bring_to_front(self) -> None`
- `cancel_pick_locator(self) -> None`
- `check(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `clear_console_messages(self) -> None`
- `clear_page_errors(self) -> None`
- `click(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `clock` — property
- `close(self, *, reason: Optional[str] = None, run_before_unload: Optional[bool] = None) -> None`
- `console_messages(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('ConsoleMessage')]`
- `content(self, *, include_shadow: Optional[bool] = None) -> str`
- `context` — property
- `dblclick(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `dispatch_event(self, selector: str, type: str, event_init: Optional[Dict] = None, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `drag_and_drop(self, source: str, target: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[playwright._impl._api_structures.Position] = None, steps: Optional[int] = None, strict: Optional[bool] = None, target_position: Optional[playwright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `emulate_media(self, *, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, media: Optional[Literal['null', 'print', 'screen']] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None) -> None`
- `eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None, *, strict: Optional[bool] = None) -> Any`
- `eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None) -> 'JSHandle'`
- `expect_console_message(self, predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]`
- `expect_download(self, predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Download')]`
- `expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager`
- `expect_file_chooser(self, predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('FileChooser')]`
- `expect_navigation(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Response')]`
- `expect_popup(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Page')]`
- `expect_request(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Request')], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Request')]`
- `expect_request_finished(self, predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Request')]`
- `expect_response(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Response')], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Response')]`
- `expect_websocket(self, predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('WebSocket')]`
- `expect_worker(self, predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager[ForwardRef('Worker')]`
- `expose_binding(self, name: str, callback: Callable) -> 'SyncContextManager'`
- `expose_function(self, name: str, callback: Callable) -> 'SyncContextManager'`
- `fill(self, selector: str, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `focus(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `frame(self, name: Optional[str] = None, *, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None) -> Optional[ForwardRef('Frame')]`
- `frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'`
- `frames` — property
- `get_attribute(self, selector: str, name: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_ref(self, ref: str) -> 'Locator'`
- `get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'`
- `get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'`
- `get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'`
- `go_back(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]`
- `go_forward(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]`
- `goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]`
- `hide_highlight(self) -> None`
- `hover(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `inner_html(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `inner_text(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `input_value(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str`
- `is_checked(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_closed(self) -> bool`
- `is_disabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_editable(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_enabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_hidden(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `is_visible(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool`
- `keyboard` — property
- `local_storage` — property
- `locator(self, selector: str, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'`
- `main_frame` — property
- `mouse` — property
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `opener(self) -> Optional[ForwardRef('Page')]`
- `page_errors(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('Error')]`
- `pause(self) -> None`
- `pdf(self, *, display_header_footer: Optional[bool] = None, footer_template: Optional[str] = None, format: Optional[str] = None, header_template: Optional[str] = None, height: Union[str, float, NoneType] = None, landscape: Optional[bool] = None, margin: Optional[playwright._impl._api_structures.PdfMargins] = None, outline: Optional[bool] = None, page_ranges: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, prefer_css_page_size: Optional[bool] = None, print_background: Optional[bool] = None, scale: Optional[float] = None, tagged: Optional[bool] = None, width: Union[str, float, NoneType] = None) -> bytes`
- `pick_locator(self) -> 'Locator'`
- `press(self, selector: str, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `query_selector(self, selector: str, *, strict: Optional[bool] = None) -> Optional[ForwardRef('ElementHandle')]`
- `query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]`
- `reload(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]`
- `remove_listener(self, event: Any, f: Any) -> None`
- `remove_locator_handler(self, locator: 'Locator') -> None`
- `request` — property
- `request_gc(self) -> None`
- `requests(self) -> List[ForwardRef('Request')]`
- `route(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any]], *, times: Optional[int] = None) -> 'SyncContextManager'`
- `route_from_har(self, har: Union[str, pathlib.Path], *, not_found: Optional[Literal['abort', 'fallback']] = None, update: Optional[bool] = None, update_content: Optional[Literal['attach', 'embed']] = None, update_mode: Optional[Literal['full', 'minimal']] = None, url: Union[str, Pattern[str], NoneType] = None) -> None`
- `route_web_socket(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Callable[[ForwardRef('WebSocketRoute')], Any]) -> None`
- `screencast` — property
- `screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, clip: Optional[playwright._impl._api_structures.FloatRect] = None, full_page: Optional[bool] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes`
- `select_option(self, selector: str, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]`
- `session_storage` — property
- `set_checked(self, selector: str, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `set_content(self, html: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None`
- `set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `set_extra_http_headers(self, headers: Dict[str, str]) -> None`
- `set_input_files(self, selector: str, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], playwright._impl._api_structures.FilePayload, Sequence[playwright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `set_viewport_size(self, viewport_size: playwright._impl._api_structures.ViewportSize) -> None`
- `tap(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `text_content(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]`
- `title(self) -> str`
- `touchscreen` — property
- `type(self, selector: str, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `uncheck(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[playwright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None`
- `unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None`
- `unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None`
- `url` — property
- `video` — property
- `viewport_size` — property
- `wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any`
- `wait_for_function(self, expression: str, *, arg: Optional[Any] = None, polling: Union[float, Literal['raf'], NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'`
- `wait_for_load_state(self, state: Optional[Literal['domcontentloaded', 'load', 'networkidle']] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]`
- `wait_for_timeout(self, timeout: Union[float, datetime.timedelta]) -> None`
- `wait_for_url(self, url: Union[str, Pattern[str], Callable[[str], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None`
- `webmcp` — property
- `workers` — property

## PageAssertions

[Official reference](https://playwright.dev/python/docs/api/class-pageassertions)

- `not_to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`
- `to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None`

## Playwright

[Official reference](https://playwright.dev/python/docs/api/class-playwright)

- `chromium` — property
- `devices` — property
- `firefox` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `request` — property
- `selectors` — property
- `stop(self) -> None`
- `webkit` — property

## Request

[Official reference](https://playwright.dev/python/docs/api/class-request)

- `all_headers(self) -> Dict[str, str]`
- `existing_response` — property
- `failure` — property
- `frame` — property
- `header_value(self, name: str) -> Optional[str]`
- `headers` — property
- `headers_array(self) -> List[playwright._impl._api_structures.NameValue]`
- `is_navigation_request(self) -> bool`
- `method` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `post_data` — property
- `post_data_buffer` — property
- `post_data_json` — property
- `redirected_from` — property
- `redirected_to` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `resource_type` — property
- `response(self) -> Optional[ForwardRef('Response')]`
- `service_worker` — property
- `sizes(self) -> playwright._impl._api_structures.RequestSizes`
- `timing` — property
- `url` — property

## Response

[Official reference](https://playwright.dev/python/docs/api/class-response)

- `all_headers(self) -> Dict[str, str]`
- `body(self) -> bytes`
- `finished(self) -> None`
- `frame` — property
- `from_service_worker` — property
- `header_value(self, name: str) -> Optional[str]`
- `header_values(self, name: str) -> List[str]`
- `headers` — property
- `headers_array(self) -> List[playwright._impl._api_structures.NameValue]`
- `http_version(self) -> str`
- `json(self) -> Any`
- `ok` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `request` — property
- `security_details(self) -> Optional[playwright._impl._api_structures.SecurityDetails]`
- `server_addr(self) -> Optional[playwright._impl._api_structures.RemoteAddr]`
- `status` — property
- `status_text` — property
- `text(self) -> str`
- `url` — property

## Route

[Official reference](https://playwright.dev/python/docs/api/class-route)

- `abort(self, error_code: Optional[str] = None) -> None`
- `continue_(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None) -> None`
- `fallback(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None) -> None`
- `fetch(self, *, headers: Optional[Dict[str, str]] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Optional[str] = None) -> 'APIResponse'`
- `fulfill(self, *, body: Union[str, bytes, NoneType] = None, content_type: Optional[str] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Any] = None, path: Union[pathlib.Path, str, NoneType] = None, response: Optional[ForwardRef('APIResponse')] = None, status: Optional[int] = None) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `request` — property

## Screencast

[Official reference](https://playwright.dev/python/docs/api/class-screencast)

- `hide_actions(self) -> None`
- `hide_overlays(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `show_actions(self, *, cursor: Optional[Literal['none', 'pointer']] = None, duration: Optional[float] = None, font_size: Optional[int] = None, position: Optional[Literal['bottom', 'bottom-left', 'bottom-right', 'top', 'top-left', 'top-right']] = None, style: Optional[playwright._impl._api_structures.ScreencastActionStyle] = None) -> 'SyncContextManager'`
- `show_chapter(self, title: str, *, description: Optional[str] = None, duration: Optional[float] = None) -> None`
- `show_overlay(self, html: str, *, duration: Optional[float] = None) -> 'SyncContextManager'`
- `show_overlays(self) -> None`
- `start(self, *, fps: Optional[int] = None, on_frame: Optional[Callable[[playwright._impl._api_structures.ScreencastFrame], Any]] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, size: Optional[playwright._impl._api_structures.ScreencastSize] = None) -> 'SyncContextManager'`
- `stop(self) -> None`

## Selectors

[Official reference](https://playwright.dev/python/docs/api/class-selectors)

- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `register(self, name: str, script: Optional[str] = None, *, content_script: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `set_test_id_attribute(self, attribute_name: str) -> None`

## Touchscreen

[Official reference](https://playwright.dev/python/docs/api/class-touchscreen)

- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `tap(self, x: float, y: float) -> None`

## Tracing

[Official reference](https://playwright.dev/python/docs/api/class-tracing)

- `group(self, name: str, *, location: Optional[playwright._impl._api_structures.TracingGroupLocation] = None) -> 'SyncContextManager'`
- `group_end(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `start(self, *, aria_snapshots: Optional[bool] = None, live: Optional[bool] = None, name: Optional[str] = None, screen_snapshots: Optional[bool] = None, screenshots: Optional[bool] = None, snapshots: Optional[bool] = None, sources: Optional[bool] = None, title: Optional[str] = None) -> 'SyncContextManager'`
- `start_chunk(self, *, name: Optional[str] = None, title: Optional[str] = None) -> 'SyncContextManager'`
- `start_har(self, path: Union[str, pathlib.Path], *, content: Optional[Literal['attach', 'embed', 'omit']] = None, mode: Optional[Literal['full', 'minimal']] = None, url_filter: Union[str, Pattern[str], NoneType] = None) -> 'SyncContextManager'`
- `stop(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None`
- `stop_chunk(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None`
- `stop_har(self) -> None`

## Video

[Official reference](https://playwright.dev/python/docs/api/class-video)

- `delete(self) -> None`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `path(self) -> pathlib.Path`
- `remove_listener(self, event: Any, f: Any) -> None`
- `save_as(self, path: Union[str, pathlib.Path]) -> None`

## WebError

[Official reference](https://playwright.dev/python/docs/api/class-weberror)

- `error` — property
- `location` — property
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `page` — property
- `remove_listener(self, event: Any, f: Any) -> None`

## WebMCP

[Official reference](https://playwright.dev/python/docs/api/class-webmcp)

- `call_tool(self, name: str, input: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `tools(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[playwright._impl._api_structures.WebMCPTool]`

## WebSocket

[Official reference](https://playwright.dev/python/docs/api/class-websocket)

- `expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager`
- `is_closed(self) -> bool`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `url` — property
- `wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any`

## WebSocketRoute

[Official reference](https://playwright.dev/python/docs/api/class-websocketroute)

- `close(self, *, code: Optional[int] = None, reason: Optional[str] = None) -> None`
- `connect_to_server(self) -> 'WebSocketRoute'`
- `on(self, event: Any, f: Any) -> None`
- `on_close(self, handler: Callable[[Optional[int], Optional[str]], Any]) -> None`
- `on_message(self, handler: Callable[[Union[str, bytes]], Any]) -> None`
- `once(self, event: Any, f: Any) -> None`
- `protocols` — property
- `remove_listener(self, event: Any, f: Any) -> None`
- `send(self, message: Union[str, bytes]) -> None`
- `url` — property

## WebStorage

[Official reference](https://playwright.dev/python/docs/api/class-webstorage)

- `clear(self) -> None`
- `get_item(self, name: str) -> Optional[str]`
- `items(self) -> List[playwright._impl._api_structures.NameValue]`
- `on(self, event: Any, f: Any) -> None`
- `once(self, event: Any, f: Any) -> None`
- `remove_item(self, name: str) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `set_item(self, name: str, value: str) -> None`

## Worker

[Official reference](https://playwright.dev/python/docs/api/class-worker)

- `evaluate(self, expression: str, arg: Optional[Any] = None) -> Any`
- `evaluate_handle(self, expression: str, arg: Optional[Any] = None) -> 'JSHandle'`
- `expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> playwright._impl._sync_base.EventContextManager`
- `on(self, event: str, f: Callable[..., NoneType]) -> None`
- `once(self, event: str, f: Callable[..., NoneType]) -> None`
- `remove_listener(self, event: Any, f: Any) -> None`
- `url` — property
