"""Page objects hold UI mechanics; test expectations remain in the tests."""

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username", exact=True)
        self.password = page.get_by_label("Password", exact=True)
        self.submit = page.get_by_role("button", name="Sign in", exact=True)
        self.message = page.locator("#login-status")

    def open(self, base_url: str):
        self.page.goto(base_url)
        return self

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
