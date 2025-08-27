# src/pages/base_page.py
from typing import Literal

from playwright.sync_api import Page

from src.elements.element_descriptor import Element
from src.utils.playwright_sync_page_screenshots import PageScreenshot
from src.clients.api_checks import URLHealth



class BasePage:

# ==========   INIT   =========================================

    def __init__(self, page: Page, url: str, unique_page_definer: str | None = None):
        self.page = page
        self.url = url
        self.unique_page_definer = unique_page_definer
        self._validate_elements()


# ==========   PAGE ACTIONS   =========================================

    def open(self):
        self.page.goto(self.url)
        #self.page.goto(self.url, wait_until="domcontentloaded") # this waiting_until is for DOMContentLoaded without loading any resources

    def back(self):
        self.page.go_back()

    def refresh(self, wait_until: Literal["load", "domcontentloaded", "networkidle"] = "load", retries: int = 1):
        """
        Literal allows the following wait_until options:
        "load" - Waits for the 'load' event. All resources including HTML, CSS, JS, images, fonts, and iframes are fully loaded.
             Use this when you need the page completely rendered and stable. Slower on heavy pages.
        "domcontentloaded" - Waits for the 'DOMContentLoaded' event. Only HTML and DOM are ready. Faster than "load".
             Images, styles, fonts, and AJAX requests may still be loading. Use this when working with DOM elements is sufficient.
        "networkidle" - Waits until there are no network requests (XHR/fetch, CSS, JS, fonts, images/video/audio, iframe requests, WebSocket)
             for a short period (~500 ms). Useful for dynamic pages SPAs (e.g. via AJAX). Can timeout if the page continuously makes network requests.
        """
        attempt = 0
        while attempt <= retries:
            try:
                self.page.reload(wait_until=wait_until)
                if self.unique_page_definer:
                    self.page.wait_for_selector(self.unique_page_definer)
                return
            except Exception as e:
                attempt += 1
                if attempt > retries:
                    raise RuntimeError(
                        f"\n[DEV LOG]\t\
                        Page {self.__class__.__name__} refresh failed after {retries} retries with exception: \n{e}"
                    ) from e    # this line show that the original cause of the RuntimeError is the TimeoutError
                print(
                    f"\n[DEV LOG]\t\
                    Warning: refresh attempt {attempt} of th page {self.__class__.__name__} is failed, retrying..."
                )

    def screenshot(self):
        return PageScreenshot(self.page).take_screenshot()


# ==========   PAGE CONTENT VALIDATION   =========================================

    # this method uses descriptor Element, which I decided to postpone
    def _validate_elements(self):
        for name, attr in self.__class__.__dict__.items(): # dictionary of page class attributes incl. class attributes, methods, descriptors
            if isinstance(attr, Element):
                page_element = getattr(self, name) # at this point, __get__ from Element is called because it is descriptor
                _ = page_element.locator


# ==========   PAGE URL CHECKS   =========================================

    def _url_health_check(self) -> tuple[int, str]:
        return URLHealth(self.url).response_basics()

    def _print_url_status(self):
        print(f"\n[DEV LOG]\tURL for {self.__class__.__name__} is: {self.url}, \
        \n\t\t\tURL Health Status is: {self._url_health_check()}")


# ==========   ADDITIONAL CHECKS   =========================================

    def _is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def _is_opened(self) -> bool:
        if not self.unique_page_definer:
            raise ValueError(
                f"\n[DEV LOG]\t\
                \"unique_page_definer\" is not set for the page object {self.__class__.__name__}"
            )
        return (
                self.url in self.page.url
                and
                self._is_element_visible(self.unique_page_definer)
        )


# ======================================================================================
# Redundant function because are implemented in every element type as individual actions

    def _click(self, selector: str):
        self.page.click(selector)

    def _fill(self, selector: str, text: str):
        self.page.fill(selector, text)
