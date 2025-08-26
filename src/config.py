# src/config.py
import pyautogui
from typing import Dict, List
from pydantic_settings import BaseSettings

from src.utils.project_paths import ProjectPaths


class Settings(BaseSettings):
    BASE_URL: str = "https://api.example.com" # default value for base url of the project
    ENV: str = "test" # default value for test run environment

    BROWSER: str = "chromium"
    HEADLESS: bool = False

    #TIMEOUT: int = 10
    default_timeout: int = 15 * 1000
    default_navigation_timeout: int = 30 * 1000

    _width, _height = pyautogui.size()
    VIEWPORT: Dict[str, int] = {"width": _width, "height": _height}
    SCREEN: Dict[str, int] = {'width': _width, 'height': _height, 'x': -5, 'y': 0}
    ARGS: List[str] = [
        f"--window-position=-5,0",
        f"--window-size={_width},{_height}"
    ]

    ignore_https_errors: bool = True
    trace: str ="on" # can be removed because it does not exist for browser.new_context() where intended to use if pytest fixtures
    video: str = "retain-on-failure"
    screenshot: str = "only-on-failure"

    session_reuse: str = "off"


    class Config:
        env_file = str(ProjectPaths().BASE_DIR / ".env")


# Usage:
# from src.config import Settings
# settings = Settings()
# x_str = settings.BASE_URL
