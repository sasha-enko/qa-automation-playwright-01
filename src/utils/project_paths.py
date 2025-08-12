# src/utils/project_paths.py
from pathlib import Path


class ProjectPaths():
    BASE_DIR = Path(__file__).resolve().parents[2]

    SRC_DIR: str = BASE_DIR / 'src'
    CLIENTS_DIR: str = SRC_DIR / 'clients'
    DB_DIR: str = SRC_DIR / 'db'
    PAGES_DIR: str = SRC_DIR / 'pages'

    TEST_DIR: str = BASE_DIR / 'tests'
    TEST_SS_DIR: str = TEST_DIR / '.screenshots'
    TEST_API_DIR: str = TEST_DIR / 'api'
    TEST_DB_DIR: str = TEST_DIR / 'db'
    TEST_ASYNC_DIR: str = TEST_DIR / 'ui' / 'async'
    TEST_SYNC_DIR: str = TEST_DIR / 'ui' / 'sync'

print(f'ProjectPaths.py name is\t{__name__}')

# Usage:
# from src.utils.project_paths import ProjectPaths
# paths = ProjectPaths()
# source_dir = paths.SRC_DIR
