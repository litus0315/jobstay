from datetime import datetime

from domain.job.job_schema import JobCreate, JobModify
from models import Job, City
from sqlalchemy.orm import Session


def get_job_list(db: Session, skip: int = 0, limit: int = 10):
    job_list = db.query(Job).order_by(Job.create_date.desc())

    total = job_list.count()
    job_list = job_list.offset(skip).limit(limit).all()

    return total, job_list


def get_job(db: Session, job_id: int):
    job = db.query(Job).get(job_id)
    return job


def create_job(db: Session, job_create: JobCreate):
    db_job = Job(subject=job_create.subject,
                 content=job_create.content,
                 password=job_create.password,
                 sido=job_create.sido,
                 gugun=job_create.gugun,
                 create_date=datetime.now())
    db.add(db_job)
    db.commit()


def modify_job(db: Session, db_job: Job, job_modify: JobModify):
    print("job modify crud")

    db_job.subject = job_modify.subject
    db_job.content = job_modify.content
    db_job.sido = job_modify.sido
    db_job.gugun = job_modify.gugun
    db.add(db_job)
    db.commit()


def get_city_list(db: Session, sido_name: str = None):
    city_sido = db.query(City.sido).distinct().all()
    sido_list = []
    gugun_list = []

    for city in city_sido:
        sido_list.append(city.sido)

    if sido_name:
        print("sido name being")
        city_gugun = db.query(City).filter(City.sido == sido_name).all()
        for city in city_gugun:
            tmp = city.gugun.split()
            if len(tmp) > 1:
                gugun_list.append(tmp[1])

    return [sido_list, gugun_list]
