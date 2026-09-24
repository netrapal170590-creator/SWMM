"""Basic home page object example."""

from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def open(self) -> None:
        self.page.goto(self.base_url)

    def title(self) -> str:
        return self.page.title()
