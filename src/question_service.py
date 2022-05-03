from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from sqlalchemy.orm import Session

from . import models
from . import schemas
from .category_service import category_service, CategoryService
from .random_api import random_api, RandomApi


class QuestionService:
    def __init__(
            self,
            random_api: RandomApi,
            category_service: CategoryService
    ):
        self.random_api = random_api
        self.category_service = category_service

    def create(
            self,
            db: Session,
            obj_in: schemas.QuestionCreate
    ) -> models.Question:
        category = category_service.get_or_create(
            db=db,
            obj_in=obj_in.category
        )
        del obj_in.category

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = models.Question(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def find(
            self,
            db: Session,
            limit: int
    ) -> List[models.Question]:
        return db.query(models.Question) \
            .order_by(desc(models.Question.saved_at)) \
            .limit(limit) \
            .all()

    def get_by_id(
            self,
            db: Session,
            id: int
    ) -> models.Question:
        return db.query(models.Question) \
            .filter(models.Question.id == id) \
            .first()

    def save_unique_question(self, db: Session, question: schemas.Question):
        question_in_db = self.get_by_id(db=db, id=question.id)

        if question_in_db is None:
            return self.create(
                db=db,
                obj_in=schemas.QuestionCreate(
                    **question.__dict__
                )
            )
        else:
            while True:
                question_new = self.random_api.get_questions(count=1)[0]

                question_in_db = self.get_by_id(db=db, id=question_new.id)

                if question_in_db is None:
                    return self.create(
                        db=db,
                        obj_in=schemas.QuestionCreate(
                            **question_new.__dict__
                        )
                    )

    def get_and_save_questions(self, db: Session, count: int):
        questions = self.random_api.get_questions(count=count)

        for question in questions:
            self.save_unique_question(db=db, question=question)


question_service = QuestionService(
    random_api=random_api,
    category_service=category_service
)
