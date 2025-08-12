from playwright.sync_api import Page
from src.utils.playwright_sync_page_screenshots import PageScreenshot
from src.clients.api_checks import URLHealth


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url


    def open(self):
        self.page.goto(self.url)

    # ----------------------------------------

    def _url_health_check(self) -> tuple[int, str]:
        return URLHealth(self.url).response_basics()


    def _print_url_status(self):
        print(f"\n[DEV LOG]\tURL for {self.__class__.__name__} is: {self.url}, \
        \n\t\t\tURL Health Status is: {self._url_health_check()}")

    # ----------------------------------------

    def _is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def _click(self, selector: str):
        self.page.click(selector)

    def _fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def _press_enter(self, selector: str):
        element = (self.page.locator(selector))
        element.press("Enter")

# ----------------------------------------

    def screenshot(self):
        return PageScreenshot(self.page)
