from sqlalchemy import Column, BigInteger, DateTime, String, Integer

from ..db.base import Base


class Category(Base):
    id = Column(BigInteger, primary_key=True)
    title = Column(String())
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    clues_count = Column(Integer)
