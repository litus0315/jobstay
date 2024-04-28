from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from domain.job import job_crud
from domain.member import member_schema

router = APIRouter(
    prefix="/api/member",
)


@router.post("/password_confirm")
def password_confirm(request_body: member_schema.PasswordConfirm,
                     db: Session = Depends(get_db)):

    job = job_crud.get_job(db, job_id=request_body.job_id)
    print(request_body.job_id, request_body.password, job.password)

    if job.password == request_body.password:
        print("Password Right")
        return True
    else:
        print("Password Wrong")
        return False

