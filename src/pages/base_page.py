# src/pages/base_page.py
from playwright.sync_api import Page

from src.elements.element_descriptor import Element
from src.utils.playwright_sync_page_screenshots import PageScreenshot
from src.clients.api_checks import URLHealth


class BasePage:
    def __init__(self, page: Page, url: str, unique_page_definer: str | None = None):
        self.page = page
        self.url = url
        self.unique_page_definer = unique_page_definer
        self._validate_elements()


    def open(self):
        self.page.goto(self.url)
        #self.page.goto(self.url, wait_until="domcontentloaded") # this waiting_until is for DOMContentLoaded without loading any resources

    def screenshot(self):
        return PageScreenshot(self.page).take_screenshot()

    # ----------------------------------------

    def _validate_elements(self):
        for name, attr in self.__class__.__dict__.items(): # dictionary of page class attributes incl. class attributes, methods, descriptors
            if isinstance(attr, Element):
                page_element = getattr(self, name) # at this point, __get__ from Element is called because it is descriptor
                _ = page_element.locator

    # ----------------------------------------

    def _url_health_check(self) -> tuple[int, str]:
        return URLHealth(self.url).response_basics()

    def _print_url_status(self):
        print(f"\n[DEV LOG]\tURL for {self.__class__.__name__} is: {self.url}, \
        \n\t\t\tURL Health Status is: {self._url_health_check()}")

    # ----------------------------------------

    def _is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def _is_opened(self) -> bool:
        if not self.unique_page_definer:
            raise ValueError(f"\n[DEV LOG]\t\"unique_page_definer\" is not set for the page object {self.__class__.__name__}")
        return (
                self.url in self.page.url
                and
                self._is_element_visible(self.unique_page_definer)
        )


    def _press_enter(self, selector: str):
        element = (self.page.locator(selector))
        element.press("Enter")

    def _back(self):
        self.page.go_back()


# ======================================================================================
# Redundant function because are implemented in every element type as individual actions

    def _click(self, selector: str):
        self.page.click(selector)

    def _fill(self, selector: str, text: str):
        self.page.fill(selector, text)
