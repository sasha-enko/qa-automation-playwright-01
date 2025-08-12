# src/utils/helpers.py
from playwright.async_api import (
    Page as AsyncPage,
    TimeoutError as AsyncTimeoutError,
)
from playwright.sync_api import (
    Page as SyncPage,
    TimeoutError as SyncTimeoutError,
)

from src.config import Settings


# =============================================================================

REJECT_BUTTON_SELECTOR = "button:has-text('Rechazar todo')"

# === Async functions ===

async def apply_default_timeouts_to_async(page: AsyncPage) -> None:
    """Apply default timeouts from CONFIG to a Playwright page instance."""
    settings = Settings()
    await page.set_default_timeout(settings.default_timeout)
    await page.set_default_navigation_timeout(settings.default_navigation_timeout)


async def reject_cookies_if_present_on_async(page: AsyncPage, selector: str = REJECT_BUTTON_SELECTOR):
    try:
        await page.click(selector, timeout=3000)
    except AsyncTimeoutError:
        pass


# === Sync functions ===

def apply_default_timeouts_to_sync(page: SyncPage) -> None:
    """Apply default timeouts from CONFIG to a synchronous Playwright page instance."""
    settings = Settings()
    page.set_default_timeout(settings.default_timeout)
    page.set_default_navigation_timeout(settings.default_navigation_timeout)


def reject_cookies_if_present_on_sync(page: SyncPage, selector: str = REJECT_BUTTON_SELECTOR):
    try:
        page.click(selector, timeout=3000)
    except SyncTimeoutError:
        pass


# Usage:
# from src.utils.helpers import (
#     apply_default_timeouts_to_async,
#     apply_default_timeouts_to_sync,
#     reject_cookies_if_present_on_async,
#     reject_cookies_if_present_on_sync,
# )
