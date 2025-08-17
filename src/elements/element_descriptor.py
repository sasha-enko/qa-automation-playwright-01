# src/elements/element_descriptor.py
from typing import Type


class Element:
    def __init__(self, selector: str, element_class: Type):
        self.selector = selector
        self.element_class = element_class

    def __get__(self, instance, owner):
        # if instance is None:
        #     return self
        return self.element_class(instance.page, self.selector)


# Usage:
# submit_btn = Element("#submit", Button)
