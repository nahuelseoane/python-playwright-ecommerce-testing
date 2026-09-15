from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.get_by_placeholder("Search")
        self.product_names = page.get_by_role("heading", level=5)

    def load(self) -> None:
        self.page.goto("/")
