from datetime import datetime

from sqlalchemy import Column, BigInteger, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from ..db.base import Base


class Question(Base):
    id = Column(BigInteger, primary_key=True)
    answer = Column(String())
    question = Column(String())
    value = Column(Integer)
    airdate = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    category_id = Column(BigInteger, ForeignKey('category.id'))
    game_id = Column(Integer)
    invalid_count = Column(Integer)

    saved_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    category = relationship("Category")
