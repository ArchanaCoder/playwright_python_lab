"""A thin HTTP client: no assertions hidden inside the client."""

from playwright.sync_api import APIRequestContext


class PaymentsClient:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def create(self, name: str, amount=100):
        return self.request.post("/api/items", data={"name": name, "amount": amount})

    def get(self, item_id: str):
        return self.request.get(f"/api/items/{item_id}")

    def delete(self, item_id: str):
        return self.request.delete(f"/api/items/{item_id}")
