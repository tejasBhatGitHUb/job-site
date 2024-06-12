from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, INTEGER, DateTime, func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
load_dotenv()


class JobApplication(Base):
    __tablename__ = "job_applications"
    job_id = Column('job_id', INTEGER, ForeignKey('jobs.id'), primary_key=True)
    user_id = Column('user_id', INTEGER, ForeignKey('users.id'), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    applicants = relationship("Job", backref='applicants')
    applied = relationship("User", backref="applied")
