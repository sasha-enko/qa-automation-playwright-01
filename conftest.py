import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Generator, AsyncGenerator
import pytest
import getpass

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
from src.utils.storage_state_args import StateArgs
from src.utils.helpers import (
    apply_default_timeouts_to_async,
    apply_default_timeouts_to_sync,
    reject_cookies_if_present_on_async,
    reject_cookies_if_present_on_sync,
)
from src.urls_resolver import get_url_for
from src.credentials_resolver import users, creds_for_user


# =========================================================================

ALLURE_DIR = str(ProjectPaths.ALLURE_REPORTS_DIR)
create_dir_if_not_exist(ALLURE_DIR)

# =========================================================================

def pytest_configure(config):
    # Check if the --alluredir option (Allure results directory) was set via CLI.
    # If not set, assign a default value (ALLURE_DIR)
    # Example of the command: pytest -s --alluredir=reports/allure tests/ui/sync/test_home_page.py::test_home_page_logo
    #
    if not getattr(config.option, "alluredir", None):
        config.option.alluredir = str(ALLURE_DIR)

# ---------------------------------

def pytest_addoption(parser):
    parser.addoption("--user", action="store", default=None, help="This the nickname of the user")


@pytest.fixture(scope="session")
def user_nickname_from_cli(request) -> str:
    return str(request.config.getoption("--user"))

# ---------------------------------

@pytest.fixture(scope="session")
def config_settings() -> Settings:
    return Settings()

# ---------------------------------

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

# ---------------------------------

@pytest.fixture
def trace_path_name(request) -> str:
    create_dir_if_not_exist(ProjectPaths.TEST_TRACE_DIR)

    test_name = request.node.name   # "request" is the pytest fixture, node.name provides the test name

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_test_name = re.sub(r'[^a-zA-Z0-9_-]', '_', test_name)
    # Why? Pytest test names can contain spaces, brackets, or other characters
    # that are unsafe for filenames. We replace them with underscores.
    # The regex replaces any character that is not a-z, A-Z, 0-9, underscore, or dash with an underscore.

    return f"{ProjectPaths.TEST_TRACE_DIR}/trace_{safe_test_name}_{timestamp}.zip"


@pytest.fixture(scope="session")
def state_args(user_nickname_from_cli: str | None = None) -> StateArgs:

    if user_nickname_from_cli:
        # gets credentials per the nickname, but before it checks its presence in 'credentials.yaml'
        username, _ = creds_for_user(user_nickname_from_cli)
        safe_usr = re.sub(r'[^a-zA-Z0-9_-]', '_', username)
    else:
        # If the key is not passed, we take the system user
        system_user = getpass.getuser()
        safe_usr = re.sub(r'[^a-zA-Z0-9_-]', '_', system_user)

    state_file = Path(f"{ProjectPaths.STORAGE_STATES_DIR}/auth_{safe_usr}.json")

    return StateArgs(storage_state=state_file, file_exists=state_file.exists())


@pytest.fixture(scope="session")
def authorization(page: SyncPage):
    login_url = get_url_for('login')
    usr_selector = ""
    pwd_selector = ""
    submit_btn = ""
    usr_name = ""
    pwd_value = ""

    page.goto(login_url)
    page.fill(usr_selector, usr_name)
    page.fill(pwd_selector, pwd_value)
    page.click(submit_btn)


# =========================================================================
# Sync Functions
# =========================================================================

@pytest.fixture(scope="session")
def sync_playwright_instance() -> Generator[SyncPlaywright, Any, None]:
    p = sync_playwright().start()

    yield p
    p.stop()


@pytest.fixture(scope="session")
def sync_browser(sync_playwright_instance: SyncPlaywright, config_settings, browser_args: dict) -> Generator[SyncBrowser, Any, None]:
    browser_type = getattr(sync_playwright_instance, config_settings.BROWSER)
    browser = browser_type.launch(**browser_args)

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def sync_context(sync_browser: SyncBrowser, browser_context_args: dict, state_args: StateArgs, config_settings: Settings) -> Generator[SyncBrowserContext, Any, None]:
    session_reuse_enabled = config_settings.session_reuse.lower() == "on"

    context_args = {**browser_context_args}
    if session_reuse_enabled:
        context_args.update(state_args.as_kwargs()) # add {"storage_state": file_path} if the file already exists

    context = sync_browser.new_context(**context_args)

    yield context

    if session_reuse_enabled:
        context.storage_state(path=str(state_args.storage_state))   # set path= to the state_file as str (note: initially returned as Path)
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
