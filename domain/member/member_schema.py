import datetime

from pydantic import BaseModel, field_validator


class PasswordConfirm(BaseModel):
    job_id: int
    password: str

