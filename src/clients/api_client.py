# src/clients/api_client.py
import requests
import httpx
from src.config import Settings

settings = Settings()

# Sync client: requests
class RequestsApiClient:
    def __init__(self, base_url: str = settings.BASE_URL):
        self.base_url = base_url

    def get_user(self, user_id: int):
        r = requests.get(f"{self.base_url}/users/{user_id}")
        r.raise_for_status()
        return r.json()

# Async client: httpx
class HttpxApiClient:
    def __init__(self, base_url: str = settings.BASE_URL):
        self.base_url = base_url

    async def get_user(self, user_id: int):
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            r = await client.get(f"/users/{user_id}")
            r.raise_for_status()
            return r.json()
