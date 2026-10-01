"""Shared Playwright fixtures."""

import pytest
from playwright.sync_api import Page

from config.config import BASE_URL, HEADLESS
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    return {"headless": HEADLESS}


@pytest.fixture
def configured_page(page: Page) -> Page:
    page.set_default_timeout(10_000)
    return page


@pytest.fixture
def home_page(configured_page: Page, base_url: str) -> HomePage:
    return HomePage(configured_page, base_url)
