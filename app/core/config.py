from typing import Optional

from pydantic_settings import BaseSettings
from app.core.env import settings

# Re-export settings for backward compatibility
app_settings = settings.app


class Settings(BaseSettings):
    APP_NAME: str = "RagE"
    APP_VERSION: str = "0.1.0"
    admin_email: str = "admin@example.com"
    items_per_page: int = 50
    debug: bool = False
    DATABASE_URL: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
