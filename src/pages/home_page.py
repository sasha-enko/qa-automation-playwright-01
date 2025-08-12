# src/pages/home_page.py
from playwright.sync_api import Page
from src.pages.base_page import BasePage
from src.urls_resolver import get_url_for


class HomePageSync(BasePage):

    HOME_URL = get_url_for('home')
    # selectors
    LOGO_IMAGE = "css=img#logo"


    def __init__(self, page: Page):
        super().__init__(page, self.HOME_URL)


    def has_logo(self) -> bool:
        return self._is_element_visible(self.LOGO_IMAGE)
