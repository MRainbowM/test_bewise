from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import models
from . import schemas


class CategoryService:
    def get_or_create(
            self,
            db: Session,
            obj_in: schemas.CategoryCreate
    ) -> models.Category:
        category_in_db = self.get_by_id(db=db, id=obj_in.id)

        if category_in_db is not None:
            return category_in_db

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = models.Category(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_id(
            self,
            db: Session,
            id: int
    ) -> models.Category:
        return db.query(models.Category) \
            .filter(models.Category.id == id) \
            .first()


category_service = CategoryService()
