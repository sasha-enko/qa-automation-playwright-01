# src/elements/button.py
from src.elements.base_element import BaseElement
from src.elements.element_decorators import with_timeout



class Button(BaseElement):

    @with_timeout
    def click(self, *, timeout: int | None = None):
        self.locator.click(timeout=timeout)

    @with_timeout
    def double_click(self, *, timeout: int | None = None):
        self.locator.dblclick(timeout=timeout)

    @with_timeout
    def right_click(self, *, timeout: int | None = None):
        self.locator.click(button="right", timeout=timeout)

    @with_timeout
    def shift_click(self, *, timeout: int | None = None):
        self.locator.click(modifiers="Shift", timeout=timeout)

    @with_timeout
    def control_click(self, *, timeout: int | None = None):
        self.locator.click(modifiers="Control", timeout=timeout)

    @with_timeout
    def long_click(self, *, timeout: int | None = None):
        self.locator.click(delay=1000, timeout=timeout)

    @with_timeout
    def press_enter(self, *, timeout: int | None = None):
        self.locator.press("Enter")
