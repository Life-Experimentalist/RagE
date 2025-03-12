from typing import Optional

from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    DB_TYPE: str = "postgres"  # postgres, mysql, sqlite
    DB_HOST: str = "localhost"
    DB_PORT: Optional[int] = None
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_NAME: Optional[str] = None

    model_config = {
        "env_file": ".env",
        "env_prefix": "",  # No prefix, we use explicit variable names
        "extra": "ignore",  # Allow extra fields from env
    }

    def get_connection_url(self) -> str:
        """Generate database connection URL based on the database type"""
        if self.DB_TYPE == "sqlite":
            return f"sqlite:///./{self.DB_NAME or 'app'}.db"

        # Default ports if not specified
        port_map = {"postgres": 5432, "mysql": 3306}
        port = self.DB_PORT or port_map.get(self.DB_TYPE, "")

        if self.DB_TYPE == "postgres":
            return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{port}/{self.DB_NAME}"
        elif self.DB_TYPE == "mysql":
            return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{port}/{self.DB_NAME}"
        raise ValueError(f"Unsupported database type: {self.DB_TYPE}")


class AppSettings(BaseSettings):
    APP_NAME: str = "RagE"
    APP_VERSION: str = "0.1.0"
    ADMIN_EMAIL: str = "admin@example.com"
    ITEMS_PER_PAGE: int = 50
    DEBUG: bool = False
    SECRET_KEY: str = "your_secret_key"
    ALLOWED_HOSTS: str = "localhost,127.0.0.1"
    PORT: int = 8000
    ENV: str = "development"

    model_config = {
        "env_file": ".env",
        "env_prefix": "",  # No prefix, we use explicit variable names
        "extra": "ignore",  # Allow extra fields from env
    }


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()

    model_config = {
        "env_file": ".env",
        "extra": "ignore",  # Allow extra fields from env
    }


# Single instance to be imported by other modules
settings = Settings()
