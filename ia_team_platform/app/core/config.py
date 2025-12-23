from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "IA Team Platform"
    ENV: str = "production"

    DATABASE_URL: str
    REDIS_URL: str

    OPENAI_API_KEY: str
    LLM_PROVIDER: str = "openai"

    class Config:
        env_file = ".env"

settings = Settings()
