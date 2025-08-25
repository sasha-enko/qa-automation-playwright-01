import re
from datetime import datetime
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
from src.utils.project_paths import ProjectPaths, create_dir_if_not_exist
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
        #"trace": config_settings.trace,
    }


@pytest.fixture
def trace_path_name(request) -> str:
    create_dir_if_not_exist(ProjectPaths.TEST_TRACE_DIR)

    test_name = request.node.name   # "request" is the pytest fixture, node.name provides the test name
    safe_test_name = re.sub(r'[^a-zA-Z0-9_-]', '_', test_name)
    # Why? Pytest test names can contain spaces, brackets, or other characters
    # that are unsafe for filenames. We replace them with underscores.
    # The regex replaces any character that is not a-z, A-Z, 0-9, underscore, or dash with an underscore.

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{ProjectPaths.TEST_TRACE_DIR}/trace_{safe_test_name}_{timestamp}.zip"


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


@pytest.fixture(scope="function")
def sync_context(sync_browser: SyncBrowser, browser_context_args) -> Generator[SyncBrowserContext, Any, None]:
    context = sync_browser.new_context(**browser_context_args)

    yield context
    context.close()


@pytest.fixture(scope="function")
def sync_context_with_trace(sync_context: SyncBrowserContext, trace_path_name: str, config_settings: Settings) -> Generator[SyncBrowserContext, Any, None]:
    """
    Fixture for a context with conditional tracing.
    If tracing is enabled, it starts tracing before the test and saves the trace file after the test.
    If tracing is "off", no trace file is created.
    """
    trace_enabled = config_settings.trace.lower() == "on"
    if trace_enabled:
        sync_context.tracing.start()

    yield sync_context
    if trace_enabled:
        sync_context.tracing.stop(path=trace_path_name)


@pytest.fixture(scope="function")
def sync_page(sync_context_with_trace: SyncBrowserContext) -> Generator[SyncPage, Any, None]:
    page = sync_context_with_trace.new_page()
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


@pytest.fixture(scope="function")
async def async_context(async_browser: AsyncBrowser, browser_context_args) -> AsyncGenerator[AsyncBrowserContext, Any]:
    context = await async_browser.new_context(**browser_context_args)

    yield context
    await context.close()


@pytest.fixture(scope="function")
async def async_context_with_trace(async_context: AsyncBrowserContext, trace_path_name: str, config_settings: Settings) -> AsyncGenerator[AsyncBrowserContext, Any]:
    """
    Fixture for a context with conditional tracing.
    If tracing is enabled, it starts tracing before the test and saves the trace file after the test.
    If tracing is "off", no trace file is created.
    """
    trace_enabled = config_settings.trace.lower() == "on"
    if trace_enabled:
        await async_context.tracing.start()

    yield async_context
    if trace_enabled:
        await async_context.tracing.stop(path=trace_path_name)


@pytest.fixture(scope="function")
async def async_page(async_context_with_trace: AsyncBrowserContext) -> AsyncGenerator[AsyncPage, Any]:
    page = await async_context_with_trace.new_page()
    await apply_default_timeouts_to_async(page)
    await reject_cookies_if_present_on_async(page)

    yield page
    await page.close()
