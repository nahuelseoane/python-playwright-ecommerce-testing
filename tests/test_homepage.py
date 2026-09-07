import re

import pytest
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_homepage_loads_successfully(page: Page) -> None:
    page.goto("https://practicesoftwaretesting.com/")

    expect(page).to_have_title(re.compile("Practice Software Testing"))
    expect(page.get_by_placeholder("Search")).to_be_visible()
    expect(page.locator("a[href^='/product/']").first).to_be_visible()
