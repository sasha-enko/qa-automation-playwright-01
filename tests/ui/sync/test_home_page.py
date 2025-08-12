import pytest

from src.pages.home_page import HomePageSync


@pytest.mark.ui
@pytest.mark.ui_sync
def test_home_page_logo(sync_page):
    page = HomePageSync(sync_page)
    page._print_url_status()
    page.open()
    assert page.has_logo() == False
