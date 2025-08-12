from typing import Dict, Any
import pytest

from playwright.async_api import Page as AsyncPage
from playwright.sync_api import Page as SyncPage

from src.config import Settings
from src.utils.playwright_sync_page_screenshots import PageScreenshot
from src.utils.helpers import (
    apply_default_timeouts_to_async,
    apply_default_timeouts_to_sync,
    reject_cookies_if_present_on_async,
    reject_cookies_if_present_on_sync,
)

# =========================================================================

@pytest.fixture
def sync_page_screenshot(custom_sync_page):
    return PageScreenshot(custom_sync_page)

# --------------------------------------------

@pytest.fixture(scope="session")
def browser_launch_args() -> Dict[str, Any]:    # fixture name is standard and predefined in pytest-playwright
    settings = Settings()
    return {
        "headless": settings.HEADLESS,
        "args": settings.ARGS
    }


@pytest.fixture(scope="session")
def browser_context_args() -> Dict[str, Any]:   # fixture name is standard and predefined in pytest-playwright
    settings = Settings()
    return {
        "viewport": settings.VIEWPORT,
        "screen": settings.SCREEN,
        "ignore_https_errors": settings.ignore_https_errors,
    }

# --------------------------------------------

@pytest.fixture
async def custom_async_page(page: AsyncPage) -> AsyncPage:

    await apply_default_timeouts_to_async(page)
    await reject_cookies_if_present_on_async(page)

    return page


@pytest.fixture
def custom_sync_page(page: SyncPage) -> SyncPage:

    apply_default_timeouts_to_sync(page)
    reject_cookies_if_present_on_sync(page)

    return page
