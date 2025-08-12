from typing import Dict, Any, Generator, AsyncGenerator
import pytest

from playwright.async_api import (
    Playwright as AsyncPlaywright,
    async_playwright,
    Browser as AsyncBrowser,
    BrowserContext as AsyncBrowserContext,
    Page as AsyncPage,
)
from playwright.sync_api import (
    Playwright as SyncPlaywright,
    sync_playwright,
    Browser as SyncBrowser,
    BrowserContext as SyncBrowserContext,
    Page as SyncPage
)

from src.config import Settings
from src.utils.helpers import (
    apply_default_timeouts_to_async,
    apply_default_timeouts_to_sync,
    reject_cookies_if_present_on_async,
    reject_cookies_if_present_on_sync,
)

# =========================================================================

@pytest.fixture(scope="session")
def config_settings() -> Settings:
    return Settings()


@pytest.fixture(scope="session")
def browser_args(config_settings) -> Dict[str, Any]:
    return {
        "headless": config_settings.HEADLESS,
        "args": config_settings.ARGS,
    }


@pytest.fixture(scope="session")
def browser_context_args(config_settings) -> Dict[str, Any]:
    return {
        "viewport": config_settings.VIEWPORT,
        "screen": config_settings.SCREEN,
        "ignore_https_errors": config_settings.ignore_https_errors,
    }

# =========================================================================
# Sync Functions
# =========================================================================

@pytest.fixture(scope="session")
def sync_playwright_instance() -> Generator[SyncPlaywright, Any, None]:
    p = sync_playwright().start()

    yield p
    p.stop()


@pytest.fixture(scope="session")
def sync_browser(sync_playwright_instance: SyncPlaywright, config_settings, browser_args) -> Generator[SyncBrowser, Any, None]:
    browser_type = getattr(sync_playwright_instance, config_settings.BROWSER)
    browser = browser_type.launch(**browser_args)

    yield browser
    browser.close()


@pytest.fixture(scope="session")
def sync_context(sync_browser: SyncBrowser, browser_context_args) -> Generator[SyncBrowserContext, Any, None]:
    context = sync_browser.new_context(**browser_context_args)

    yield context
    context.close()


@pytest.fixture
def sync_page(sync_context: SyncBrowserContext) -> Generator[SyncPage, Any, None]:
    page = sync_context.new_page()
    apply_default_timeouts_to_sync(page)
    reject_cookies_if_present_on_sync(page)

    yield page
    page.close()


# =========================================================================
# Async Functions
# =========================================================================


@pytest.fixture(scope="session")
async def async_playwright_instance() -> AsyncGenerator[AsyncPlaywright, Any]:
    p = await async_playwright().start()

    yield p
    await p.stop()


@pytest.fixture(scope="session")
async def async_browser(async_playwright_instance: AsyncPlaywright, config_settings, browser_args) -> AsyncGenerator[AsyncBrowser, Any]:
    browser_type = await getattr(async_playwright_instance, config_settings.BROWSER)
    browser = await browser_type.launch(**browser_args)

    yield browser
    await browser.close()


@pytest.fixture(scope="session")
async def async_context(async_browser: AsyncBrowser, browser_context_args) -> AsyncGenerator[AsyncBrowserContext, Any]:
    context = await async_browser.new_context(**browser_context_args)

    yield context
    await context.close()


@pytest.fixture
async def async_page(async_context: AsyncBrowserContext) -> AsyncGenerator[AsyncPage, Any]:
    page = await async_context.new_page()
    await apply_default_timeouts_to_async(page)
    await reject_cookies_if_present_on_async(page)

    yield page
    await page.close()
