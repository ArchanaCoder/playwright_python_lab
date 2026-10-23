# Local REST API quick reference

The base URL is printed by the manual server (normally http://127.0.0.1:8765).
Pytest uses a different free port and passes it through the `base_url` fixture.

| Method | Route | Purpose | Auth |
| --- | --- | --- | --- |
| GET | `/health` | Readiness JSON | No |
| POST | `/api/login` | JSON or form username/password; returns token and session cookie | No |
| POST | `/api/logout` | Invalidate the cookie session and remove its cookie | Cookie |
| GET | `/api/me` | Current demo user | Cookie or bearer |
| GET | `/api/items?q=...` | Query payments by name | Cookie or bearer |
| POST | `/api/items` | Create with name and optional amount; returns 201 and Location | Cookie or bearer |
| GET | `/api/items/{id}` | Read one payment | Cookie or bearer |
| PUT | `/api/items/{id}` | Replace name and amount | Cookie or bearer |
| PATCH | `/api/items/{id}` | Change supplied name/amount fields | Cookie or bearer |
| DELETE | `/api/items/{id}` | Delete; returns 204 | Cookie or bearer |
| GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS | `/api/echo` | Echo payload, query and X-Learning header | No |
| POST | `/api/upload` | Multipart `file`, optional `description` | No |
| GET | `/api/status/{status}` | Selected success/error practice responses | No |
| GET | `/api/redirect` | 302 to /health | No |
| GET | `/api/text` | Plain-text response | No |
| GET | `/download` | Download a small CSV | No |

Sample create body: `{"name": "Practice transfer", "amount": 100}`.
For bearer authentication, use the token returned by login in
`Authorization: Bearer <token>`. Cookie-based requests use the automatically
stored session cookie instead. This is a single-user teaching app; numeric business
validation, tenant isolation, CSRF protection and production-grade auth are not modeled.
