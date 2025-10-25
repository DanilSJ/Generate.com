from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    db_url: str = os.environ.get(
        "DATABASE_URL", f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    )
    db_echo: bool = False


settings = Settings()
