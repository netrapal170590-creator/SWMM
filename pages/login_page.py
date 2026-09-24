"""Login page actions."""

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, base_url: str) -> None:
        self.page.goto(base_url)
        self.page.get_by_text("Login", exact=True).click()

    def login(self, username: str, password: str) -> None:
        self.page.locator("#fd").fill(username)
        self.page.locator("#pass").fill(password)
        self.page.get_by_text("Secure Login", exact=True).click()
        self.page.wait_for_url("**/afterAuth/**")
