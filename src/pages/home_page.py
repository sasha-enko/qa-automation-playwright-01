# src/pages/home_page.py
from playwright.sync_api import Page
from src.urls_resolver import get_url_for

from src.pages.base_page import BasePage
from src.pages.home_page_selectors import (
    HomePageSelectors as SelectorFor,
    HomePagePanelNames as PanelName
)


class HomePageSync(BasePage):
    HOME_URL = get_url_for('home')

    PANELS = {
        panel.value: f'{SelectorFor.PANEL_DIV.value}:has-text("{panel.value}")'
        for panel in PanelName
    }

    def __init__(self, page: Page):
        super().__init__(page, self.HOME_URL, SelectorFor.UNIQUE_PAGE_DEFINER.value)


# ===================================================

    def has_logo(self) -> bool:
        return self._is_element_visible(self.PANELS["Elements"])
