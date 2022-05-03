import logging
from typing import Any, Dict, Optional

import dotenv
from pydantic import BaseSettings, PostgresDsn, validator

dotenv.load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Test Bewise'

    HOST: str = '127.0.0.1'
    PORT: int = 8000

    LOG_LEVEL: int = logging.INFO

    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASS: str
    POSTGRES_DB: str

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, value: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASS'),
            host=values.get('POSTGRES_HOST'),
            path='/{}'.format(values.get('POSTGRES_DB') or ''),
        )

    RANDOM_API_URL: str = 'https://jservice.io/api/random'

    class Config:
        case_sensitive = True
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
