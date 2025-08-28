# src/elements/base_element.py
from playwright.sync_api import Locator
from playwright.sync_api import Page

from src.elements.element_enums import ElementState
from src.decorators.waits import with_timeout



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
                f"\n[DEV LOG]\t\
                Element was not found on the page {self.page.__class__.__name__}: \
                element type = {self.__class__.__name__} by selector = \"{self.selector}\""
            )
        return loc


    # this function is used in decorator with_timeout
    def _effective_timeout(self, timeout: int | None = None) -> int | None:
        # manually specified timeout -> then element_timeout -> then page default timeout which is set in fixture/pulled from config
        return timeout or self.element_timeout


    @with_timeout
    def is_visible(self, *, timeout: int | None = None) -> bool:
        return self.locator.is_visible(timeout=timeout)


    @with_timeout
    def wait_in_dom_until(self, *, attached: bool = True, timeout: int | None = None):
        state = ElementState.ATTACHED if attached else ElementState.DETACHED
        return self.locator.wait_for(state=state.value, timeout=timeout)

    @with_timeout
    def wait_on_page_until(self, *, visible: bool = True, timeout: int | None = None):
        state = ElementState.VISIBLE if visible else ElementState.HIDDEN
        return self.locator.wait_for(state=state.value, timeout=timeout)


    @with_timeout
    def get_text(self, *, timeout: int | None = None) -> str:
        return self.locator.inner_text(timeout=timeout)


    @with_timeout
    def hover(self, *, timeout: int | None = None):
        if not self.is_visible(timeout=timeout):
            raise TimeoutError(
                f"\n[DEV LOG]\t\
                After {timeout} ms\n\t\t\tElement is not visible on the page {self.page.__class__.__name__}: \
                element type = {self.__class__.__name__} by selector = \"{self.selector}\""
            )
        self.locator.hover(timeout=timeout)
