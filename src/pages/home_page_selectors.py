# src/pages/home_page_selectors.py
from enum import Enum


class HomePageSelectors(str, Enum):
    UNIQUE_PAGE_DEFINER = "footer"
    PANEL_DIV = "div.card.mt-4.top-card h5"


class HomePagePanelNames(str, Enum):
    ELEMENTS = "Elements"
    FORMS = "Forms"
    ALERTS = "Alerts"
    FRAME_AND_WINDOWS = "Frame & Windows"
    WIDGETS = "Widgets"
    INTERACTIONS = "Interactions"
    BOOK_STORE_APP = "Book Store Application"
