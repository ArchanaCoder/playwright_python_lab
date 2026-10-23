# Learn by doing — ten sessions

Suggested budget: about 60 minutes per session, not a promise of mastery in ten hours.
Each session: 10 minutes reading → 30 minutes coding → 10 minutes deliberately breaking
something → 10 minutes explaining it without looking at the code.

| Session | Read/run | Your exercise | Explain aloud |
| --- | --- | --- | --- |
| 1 | README; locators | Find one element three ways; choose the most stable | What makes a locator robust? |
| 2 | actions | Fill a form, check terms, select a country | fill vs sequential typing; native select vs custom dropdown |
| 3 | waits/assertions | Remove sleep; test delayed visibility/enabling | What does auto-waiting guarantee, and what does it not? |
| 4 | frames/files/windows | Upload, download, and read an iframe | Why register an event listener before clicking? |
| 5 | dialogs/events | Accept a prompt and inspect console output | Why can an unhandled registered dialog stall a test? |
| 6 | UI network | Mock success, failure, and modified response | Mocking vs a true integration test |
| 7 | API verbs/payloads | Send JSON, form, multipart; inspect raw response | Path vs query parameter; PUT vs PATCH |
| 8 | API auth/contracts | Reproduce 401/422/404, then full CRUD | Cookies vs bearer header; status vs business correctness |
| 9 | integration/POM | Create via API, verify via UI; add a new page action | Fixture ownership; isolation; teardown; API/client boundaries |
| 10 | advanced + CI | Inspect trace, try HAR replay and two workers | Flakiness diagnosis, parallelism, and evidence |

## First exercise, step by step

1. Run `python -m pytest tests/ui/test_02_actions.py -k checkbox --headed -v`.
2. Read that test and locate `lab` in tests/conftest.py.
3. Explain: pytest starts app → opens isolated page → checks terms → asserts state.
4. Change the final checkbox state to unchecked and update the assertion.
5. Intentionally use a wrong label. Read the failure rather than guessing.
6. Rebuild the test tomorrow from memory.

## Practice challenges (not pre-solved tests)

- Add a custom dropdown to the app and automate it with role option/listbox locators.
- Add server-side numeric validation for amount and test boundary values.
- Add pagination; create data with the API and verify the right page in the UI.
- Add a duplicate-name business rule and check a 409 response.
- Create two authenticated users and prove their data is isolated (the demo currently
  has one user and global in-memory items; it does not model tenant isolation).
- Add an explicit JSON Schema validator when response contracts become complex.
- Add one business-level BDD scenario if your target team uses BDD. Avoid duplicating
  every low-level test as a feature file; this project uses plain pytest deliberately.

## Interview self-check

Explain Browser → Context → Page; the sync/async distinction; locator strictness;
actionability vs application readiness; retrying `expect` vs immediate reads;
APIRequestContext cookie ownership; test data cleanup; and why retries can hide defects.
