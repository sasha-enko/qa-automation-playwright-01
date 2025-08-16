# src/pages/home_page.py
from playwright.sync_api import Page
from src.pages.base_page import BasePage
from src.urls_resolver import get_url_for


class HomePageSync(BasePage):

    HOME_URL = get_url_for('home')
    UNIQUE_SELECTOR = "footer"


    DIV_SELECTOR = "div.card.mt-4.top-card h5"

    def __div_locator_for(self, element_text: str) -> str:
        return f'{self.DIV_SELECTOR}:has-text("{element_text}")'


    def __init__(self, page: Page):
        super().__init__(page, self.HOME_URL, self.UNIQUE_SELECTOR)

        self.PANELS = {
            "Elements": self.__div_locator_for("Elements"),
            "Forms": self.__div_locator_for("Forms"),
            "Alerts": self.__div_locator_for("Alerts"),
            "Frame & Windows": self.__div_locator_for("Frame & Windows"),
            "Widgets": self.__div_locator_for("Widgets"),
            "Interactions": self.__div_locator_for("Interactions"),
            "Book Store Application": self.__div_locator_for("Book Store Application"),
        }

# ===================================================

    def has_logo(self) -> bool:
        return self._is_element_visible(self.PANELS["Elements"])
