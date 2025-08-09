# src/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    BASE_URL: str = "https://api.example.com"
    HEADLESS: bool = True
    BROWSER: str = "chromium"
    TIMEOUT: int = 10

    class Config:
        env_file = ".env"
