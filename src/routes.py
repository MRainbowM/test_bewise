from typing import List

from fastapi import APIRouter, Body, Depends, BackgroundTasks
from pydantic import conint
from sqlalchemy.orm import Session

from src.question_service import question_service
from .db.session import get_db
from .schemas import Question

router = APIRouter()


@router.get('/', tags=['Root'])
async def root():
    return {'message': '200 OK'}


@router.post(
    '/',
    tags=['Question'],
    response_model=List[Question],
    summary="Get quiz questions"
)
def get_question(
        *, db: Session = Depends(get_db),
        questions_num: conint(gt=0) = Body(1, embed=True),
        background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        question_service.get_and_save_questions,
        db=db,
        count=questions_num
    )

    return question_service.find(
        db=db,
        limit=questions_num
    )
