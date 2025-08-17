from src.elements.base_element import BaseElement


class Button(BaseElement):

    def click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.click(timeout=t)

    def double_click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.dblclick(timeout=t)

    def right_click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.click(button="right", timeout=t)

    def shift_click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.click(modifiers="Shift", timeout=t)

    def control_click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.click(modifiers="Control", timeout=t)

    def long_click(self, timeout: int | None = None):
        t = self._effective_timeout(timeout)
        self.locator.click(delay=1000, timeout=t)
