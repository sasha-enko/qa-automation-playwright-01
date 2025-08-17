# src/elements/base_element.py
from xml.sax.xmlreader import Locator

from playwright.sync_api import Page


class BaseElement:
    def __init__(self, page: Page, selector: str, timeout: int | None = None):
        self.page = page
        self.selector = selector
        self.element_timeout = timeout


    @property
    def locator(self) -> Locator:
        loc = self.page.locator(self.selector)
        if loc.count() == 0:
            raise ValueError(
                f"\n[DEV LOG]\tElement was not found on the page {self.page.__class__.__name__}: \
                element type = {self.__class__.__name__} by selector = \"{self.selector}\""
            )
        return loc


    def _effective_timeout(self, timeout: int | None = None) -> int | None:
        # manually specified timeout -> then element_timeout -> then page default timeout which is set in fixture/pulled from config
        return timeout or self.element_timeout


    def is_visible(self, timeout: int | None = None) -> bool:
        t = self._effective_timeout(timeout)
        return self.locator.is_visible(timeout=t)


    def wait_for(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        return self.locator.wait_for(timeout=t)


    def get_text(self, timeout: int | None = None) -> str:
        t = self._effective_timeout(timeout)
        return self.locator.inner_text(timeout=t)
