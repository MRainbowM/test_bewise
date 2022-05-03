from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SQLSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = None
    try:
        db = SQLSession()
        yield db
    finally:
        if db is not None:
            db.close()
