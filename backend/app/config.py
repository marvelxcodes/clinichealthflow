from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "HealthNivaran API"
    database_url: str = "postgresql+psycopg://healthnivaran:healthnivaran@localhost:5432/healthnivaran"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
