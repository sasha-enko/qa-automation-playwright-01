# src/utils/project_paths.py
from pathlib import Path


class ProjectPaths():
    BASE_DIR = Path(__file__).resolve().parents[2]

    REPORTS_DIR: str = BASE_DIR / 'reports'
    ALLURE_REPORTS_DIR: str = REPORTS_DIR / 'allure'

    SCRIPTS_DIR: str = BASE_DIR / 'scripts'
    SRC_DIR: str = BASE_DIR / 'src'

    CLIENTS_DIR: str = SRC_DIR / 'clients'
    DB_DIR: str = SRC_DIR / 'db'
    ELEMENTS_DIR: str = SRC_DIR / 'elements'
    PAGES_DIR: str = SRC_DIR / 'pages'
    UTILS__DIR: str = SRC_DIR / 'utils'

    STORAGE_STATES_DIR: str = BASE_DIR / 'storage_states'
    TEST_DIR: str = BASE_DIR / 'tests'

    TEST_SS_DIR: str = TEST_DIR / '.screenshots'
    TEST_TRACE_DIR: str = TEST_DIR / '.traces'
    TEST_API_DIR: str = TEST_DIR / 'api'
    TEST_DB_DIR: str = TEST_DIR / 'db'
    TEST_ASYNC_DIR: str = TEST_DIR / 'ui' / 'async'
    TEST_SYNC_DIR: str = TEST_DIR / 'ui' / 'sync'


def create_dir_if_not_exist(full_dir_path: str) -> None:
    Path(full_dir_path).mkdir(parents=True, exist_ok=True)


print(f'ProjectPaths.py name is\t{__name__}')

# Usage:
# from src.utils.project_paths import ProjectPaths
# paths = ProjectPaths()
# source_dir = paths.SRC_DIR
