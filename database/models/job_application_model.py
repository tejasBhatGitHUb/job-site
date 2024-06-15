from sqlalchemy import Column, ForeignKey, INTEGER, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base, relationship
import os
from dotenv import load_dotenv
from database.models.job_model import Job
from database.models.user_model import User

load_dotenv()
Base = declarative_base()


class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    job_id = Column('job_id', INTEGER, ForeignKey(Job.id), unique=True)
    user_id = Column('user_id', INTEGER, ForeignKey(User.id), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # applicants = relationship("Job", backref=Job.applicants)
    # applied = relationship("User", backref=User.applied)


engine = create_engine(os.getenv("connection_string"))
Base.metadata.create_all(bind=engine)
