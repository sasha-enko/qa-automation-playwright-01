from pathlib import Path
from typing import List
from playwright.sync_api import Page

from src.config import Settings
from src.utils.project_paths import ProjectPaths


class PageScreenshot():

    _pytest_ss_path: Path = ProjectPaths.TEST_SS_DIR
    _default_file_prefix: str = 'newSS_'
    _file_extension: str = '.png'

    def __init__(self, page: Page):
        self.page = page

    def __call__(self, page: Page):
        self.page = page
        self.take_screenshot()


    def take_screenshot(self) -> None:

        ss_name = self.__assign_filename()
        full_ss_path = self._pytest_ss_path / ss_name

        self.page.screenshot(path=full_ss_path)


    @classmethod
    def __pytest_screenshots_list(cls) -> List[str]:

        path = cls._pytest_ss_path

        if not path.is_dir():
            return []

        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and file.suffix == cls._file_extension
        ]


    @classmethod
    def __higher_identifier_in_list(cls) -> int:

        file_list = cls.__pytest_screenshots_list()
        cleaned_list = []

        for file in file_list:
            if file.startswith(cls._default_file_prefix) and file.endswith(cls._file_extension):

                id_str = file[len(cls._default_file_prefix):-len(cls._file_extension)]

                if id_str.isdigit():
                    cleaned_list.append(int(id_str))

        return max(cleaned_list, default=0)


    @classmethod
    def __assign_filename(cls) -> str:

        next_id = cls.__higher_identifier_in_list() + 1
        return f"{cls._default_file_prefix}{next_id:02}{cls._file_extension}"


# Usage:
# PageScreenshot(page)
# or
# ss_taker = PageScreenshot(page)
# ss_taker.take_screenshot()
