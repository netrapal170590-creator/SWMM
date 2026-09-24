"""Shared Playwright fixtures."""

import os

import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "http://172.16.40.161/landing").rstrip("/")


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    return {"headless": os.getenv("HEADLESS", "true").lower() == "true"}


@pytest.fixture
def configured_page(page: Page) -> Page:
    page.set_default_timeout(10_000)
    return page


@pytest.fixture
def home_page(configured_page: Page, base_url: str) -> HomePage:
    return HomePage(configured_page, base_url)
