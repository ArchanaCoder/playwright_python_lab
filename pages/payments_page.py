from playwright.sync_api import Page


class PaymentsPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_label("Payment name", exact=True)
        self.amount = page.get_by_label("Amount", exact=True)
        self.submit = page.get_by_role("button", name="Create payment", exact=True)
        self.message = page.locator("#payment-status")

    def create(self, name: str, amount: int):
        self.name.fill(name)
        self.amount.fill(str(amount))
        self.submit.click()

    def row(self, name: str):
        return self.page.get_by_role("row").filter(
            has=self.page.get_by_role("cell", name=name, exact=True)
        )
