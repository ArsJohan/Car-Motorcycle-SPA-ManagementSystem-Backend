from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "Auto and Motorcycle Spa Backend"
    debug: bool = False
    database_url: Optional[str] = None
    
    # Database settings
    postgres_user: str = "auto_spa_user"
    postgres_password: str = "auto_spa_password"
    postgres_db: str = "auto_spa_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    
    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def database_url_computed(self) -> str:
        """Compute database URL from components."""
        if self.database_url:
            return self.database_url
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()