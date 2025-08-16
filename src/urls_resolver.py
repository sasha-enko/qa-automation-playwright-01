# src/urls_resolver.py
import yaml
from src.config import Settings
from src.utils.project_paths import ProjectPaths


src_path = ProjectPaths().SRC_DIR

with open(src_path / 'urls.yaml', "r") as f:
    project_urls = yaml.safe_load(f)

def get_url_for(key: str) -> str:
    return Settings().BASE_URL.rstrip("/") + project_urls[key]

def get_url_ending_fragment_for(key: str) -> str:
    return project_urls[key]
