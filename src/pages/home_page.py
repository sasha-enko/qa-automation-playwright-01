# src/pages/home_page.py
from playwright.sync_api import Page

from src.urls_resolver import get_url_for
from src.elements.button import Button

from src.pages.base_page import BasePage
from src.pages.home_page_selectors import (
    HomePageSelectors as SelectorFor,
    HomePagePanelNames as PanelName
)



class HomePageSync(BasePage):
    HOME_URL = get_url_for('home')

# ==========   SELECTORS   =========================================

    # Dictionary of panel selectors
    # Key: PanelName Enum - represents the panel's name
    # Value: CSS selector string used to locate the panel on the page
    PANEL_SELECTORS = {
        panel: f'{SelectorFor.PANEL_DIV.value}:has-text("{panel.value}")'
        for panel in PanelName
    }

    LOGO = 'header a[href^="https"][href*="demoqa"]'


# ==========   INIT   =========================================

    def __init__(self, page: Page):
        super().__init__(page, self.HOME_URL, SelectorFor.UNIQUE_PAGE_DEFINER.value)

        # Dictionary of panel objects
        # Key: panel - PanelName Enum that identifies panel. Example of use: PanelName.FORMS
        # Value: Button - a Button object representing the panel
        self.panels: dict[PanelName, Button] = {
            panel: Button(page, selector)
            for panel, selector in self.PANEL_SELECTORS.items()
        }


# ==========   PAGE ACTIONS   =========================================

    def has_logo(self) -> bool:
        return self._is_element_visible(self.LOGO)
