# src/credentials_resolver.py
import yaml
from functools import lru_cache
from src.utils.project_paths import ProjectPaths



src_path = ProjectPaths().SRC_DIR
cred_config_name = 'credentials.yaml'

@lru_cache(maxsize=1)   # this ensures the credentials file is read only once, subsequent requests will refer to cached data
def users() -> dict[str, dict[str, str]]:
    with open(src_path / cred_config_name, "r") as f:
        user_credentials = yaml.safe_load(f)
    return user_credentials["users"]


def creds_for_user(user_nickname: str) -> tuple[str, str]:
    user = users().get(user_nickname)   # returns {"username": "admin", "password": "admin123"}
    if not user:
        raise ValueError(f"\nDEV LOG\tUser with nickname{user_nickname} is not found in the {cred_config_name} file")
    if "username" not in user or "password" not in user:
        raise ValueError(f"\nDEV LOG\tUser with nickname{user_nickname} is not correctly configured in {cred_config_name} file")
    username = str(user["username"])
    password = str(user["password"])
    return username, password
