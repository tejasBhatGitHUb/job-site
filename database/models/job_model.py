from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    recruiter_id = Column('admin_id', INTEGER)
    role = Column('role', VARCHAR(100))
    company = Column('company', VARCHAR(100))
    location = Column('location', VARCHAR(100))
    responsibilities = Column('responsibilities', VARCHAR(2000))
    requirements = Column('requirements', VARCHAR(2000))
    website = Column('website', VARCHAR(100))
    salary = Column('salary', INTEGER)
    perks=Column('perks',VARCHAR(150))
    min_experience = Column('min_experience', FLOAT)
    email = Column('email', VARCHAR(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, recruiter_id, role, company, location, responsibilities, requirements, website, salary,
                 min_experience,email,perks):
        self.recruiter_id = recruiter_id
        self.role = role
        self.company = company
        self.location = location
        self.responsibilities = responsibilities
        self.requirements = requirements
        self.website = website
        self.salary = salary
        self.min_experience = min_experience
        self.perks=perks
        self.email = email

        def __repr__(self):
            return f'''{self.id}, {self.admin_id},{self.role}, {self.company}, {self.location}, {self.responsibilities}, {self.requirements}, {self.website}, {self.salary}',
            {self.currency},{self.min_experience},{self.email}'''


engine = create_engine(os.getenv("connection_string"))
Base.metadata.create_all(bind=engine)