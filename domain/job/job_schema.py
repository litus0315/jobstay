import datetime

from pydantic import BaseModel, field_validator

from domain.answer.answer_schema import Answer


class Job(BaseModel):
    id: int
    sido: str
    gugun: str
    subject: str
    content: str
    password: str
    create_date: datetime.datetime
    answers: list[Answer] = []


class JobCreate(BaseModel):
    subject: str
    content: str
    sido: str
    gugun: str
    password: str

    @field_validator('subject', 'content', 'password')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class JobList(BaseModel):
    total: int = 0
    job_list: list[Job] = []


class JobModify(JobCreate):
    job_id: int


class City(BaseModel):
    id: int
    sido: str
    gugun: str
