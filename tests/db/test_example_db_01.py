from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")

def test_db_password_loaded():
    assert password is not None
    assert len(password) > 0
