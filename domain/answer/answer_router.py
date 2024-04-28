from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.job import job_crud

router = APIRouter(
    prefix="/api/answer",
)


@router.post("/create/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def answer_create(job_id: int,
                  _answer_create: answer_schema.AnswerCreate,
                  db: Session = Depends(get_db)):
    # create answer
    job = job_crud.get_job(db, job_id=job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    answer_crud.create_answer(db, job=job, answer_create=_answer_create)
