"""Basic browser test example."""

from pages.home_page import HomePage


def test_home_page_has_a_title(home_page: HomePage) -> None:
    home_page.open()

    assert home_page.title()
