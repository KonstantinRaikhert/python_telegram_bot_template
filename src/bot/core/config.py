from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for the bot."""

    telegram_token: str
    debug: bool = False

    class Config:
        """Config enviroments."""

        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
