from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    password = Column(String, nullable=False)
    sido = Column(String, nullable=False)
    gugun = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    job_id = Column(Integer, ForeignKey("job.id"))
    job = relationship("Job", backref="answers")


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    sido = Column(String, nullable=False)
    gugun = Column(String, nullable=False)

