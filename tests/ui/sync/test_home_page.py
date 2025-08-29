import allure
import pytest
from playwright.sync_api import expect
from src.pages.home_page import HomePageSync
from src.pages.home_page_selectors import HomePagePanelNames as Panel


@allure.feature("Demo Feature")
@allure.story("Demo Story")
@pytest.mark.ui
@pytest.mark.ui_sync
def test_home_page_logo(sync_page):
    with allure.step("OK: generate page"):
        page = HomePageSync(sync_page)
    with allure.step("OK: open Home page"):
        page._print_url_status()
        page.open()
    assert page._is_opened()
    with allure.step("OK: take screenshot"):
        page.screenshot()


@pytest.mark.ui
@pytest.mark.ui_sync
def test_home_page_(sync_page):
    page = HomePageSync(sync_page)
    page.open()
    assert page._is_opened()

    for card in page.panels.values():
        card.hover()
        card.click()
        page.screenshot()
        page.back()

    forms_panel = page.panels[Panel.FORMS]
    assert forms_panel.is_visible()
    expect(forms_panel.locator).not_to_be_hidden()

    assert page.has_logo()

