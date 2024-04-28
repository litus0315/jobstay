from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer.answer_schema import AnswerCreate
from models import Job, Answer


def create_answer(db: Session, job: Job, answer_create: AnswerCreate):
    db_answer = Answer(job=job,
                       content=answer_create.content,
                       create_date=datetime.now())
    db.add(db_answer)
    db.commit()