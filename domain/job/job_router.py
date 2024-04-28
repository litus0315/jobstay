from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from starlette import status
from database import get_db
from domain.job import job_schema, job_crud


router = APIRouter(
    prefix="/api/job",
)


@router.get("/list", response_model=job_schema.JobList)
def job_list(db: Session = Depends(get_db), page: int = 0, size: int = 10):
    total, _job_list = job_crud.get_job_list(
        db, skip=page * size, limit=size)

    return {
        'total': total,
        'job_list': _job_list
    }


@router.get("/detail/{job_id}", response_model=job_schema.Job)
def job_detail(job_id: int, db: Session = Depends(get_db)):
    job = job_crud.get_job(db, job_id=job_id)
    return job


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def job_create(_job_create: job_schema.JobCreate, db: Session = Depends(get_db)):
    job_crud.create_job(db=db, job_create=_job_create)


@router.post("/modify", status_code=status.HTTP_204_NO_CONTENT)
def job_modify(_job_modify: job_schema.JobModify, db: Session = Depends(get_db)):
    db_job = job_crud.get_job(db, job_id=_job_modify.job_id)

    if db_job.password != _job_modify.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="수정 권한이 없습니다.")

    if not db_job:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="데이터를 찾을수 없습니다.")

    job_crud.modify_job(db=db, db_job=db_job, job_modify=_job_modify)



@router.get("/city_data")
def get_city_data(sido_name: str = None, db: Session = Depends(get_db)):
    sido, gugun = job_crud.get_city_list(db, sido_name=sido_name)

    return {
        'sido': sido,
        'gugun': gugun
    }

