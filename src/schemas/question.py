from datetime import datetime

from pydantic import BaseModel, Field, conint

from .category import Category, CategoryCreate


class QuestionCreate(BaseModel):
    id: conint(gt=0)
    answer: str = Field()
    question: str = Field()
    value: conint(gt=0) = None
    airdate: datetime = None
    created_at: datetime
    updated_at: datetime = None
    game_id: int = None
    invalid_count: int = None
    category_id: conint(gt=0)

    category: CategoryCreate


class QuestionInDB(BaseModel):
    id: int
    answer: str
    question: str = None
    value: int = None
    airdate: datetime = None
    created_at: datetime
    updated_at: datetime = None
    game_id: int = None
    invalid_count: int = None
    category_id: int

    saved_at: datetime

    class Config:
        orm_mode = True


class Question(QuestionInDB):
    saved_at: datetime = None
    category: Category
