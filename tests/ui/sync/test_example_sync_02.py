import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.ui
@pytest.mark.ui_sync
def test_try():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        print("Playwright setup successfully")
        browser.close()
