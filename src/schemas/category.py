from datetime import datetime

from pydantic import BaseModel, Field, conint


class CategoryCreate(BaseModel):
    id: conint(gt=0)
    title: str = Field()
    created_at: datetime
    updated_at: datetime = None
    clues_count: int


class CategoryInDB(BaseModel):
    id: int
    title: str
    created_at: datetime
    updated_at: datetime = None
    clues_count: int

    class Config:
        orm_mode = True


class Category(CategoryInDB):
    pass
