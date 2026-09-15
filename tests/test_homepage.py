import re

import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage


@pytest.mark.smoke
def test_homepage_loads_successfully(page: Page) -> None:
    home_page = HomePage(page)

    home_page.load()

    expect(page).to_have_title(re.compile("Practice Software Testing"))
    expect(home_page.search_input).to_be_visible()
    expect(home_page.product_names.first).to_be_visible()
