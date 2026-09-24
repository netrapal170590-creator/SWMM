"""Login test."""

import pytest
from playwright.sync_api import Page

from config.config import BASE_URL, PASSWORD, USERNAME
from pages.login_page import LoginPage


def test_admin_can_login(page: Page) -> None:
    if not PASSWORD:
        pytest.fail("Set APP_PASSWORD before running the login test.")

    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    assert "/afterAuth/" in page.url
