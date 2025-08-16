import pytest
from playwright.sync_api import expect

from src.pages.home_page import HomePageSync


@pytest.mark.ui
@pytest.mark.ui_sync
def test_home_page_logo(sync_page):
    page = HomePageSync(sync_page)
    page._print_url_status()
    page.open()
    assert page._is_opened()
    page.screenshot()


@pytest.mark.ui
@pytest.mark.ui_sync
def test_home_page_(sync_page):
    page = HomePageSync(sync_page)
    page.open()

    for card in page.PANELS.values():
        expect(card).to_be_visible()
        page._click(card)
        page.screenshot()
        page._back()