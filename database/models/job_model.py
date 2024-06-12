from dotenv import load_dotenv
from sqlalchemy import Column,INTEGER, VARCHAR, FLOAT, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()
load_dotenv()


class Job(Base):
    __tablename__ = "jobs"
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    admin_id = Column('admin_id', INTEGER)
    role = Column('role', VARCHAR(100))
    company = Column('company', VARCHAR(100))
    location = Column('location', VARCHAR(100))
    responsibilities = Column('responsibilities', VARCHAR(2000))
    requirements = Column('requirements', VARCHAR(2000))
    website = Column('website', VARCHAR(100))
    salary = Column('salary', INTEGER)
    currency = Column('currency', VARCHAR(50))
    min_experience = Column('min_experience', FLOAT)
    email = Column('email', VARCHAR(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, admin_id, role, company, location, responsibilities, requirements, website, salary, currency,
                 min_experience,
                 email):
        self.admin_id = admin_id
        self.role = role
        self.company = company
        self.location = location
        self.responsibilities = responsibilities
        self.requirements = requirements
        self.website = website
        self.salary = salary
        self.currency = currency
        self.min_experience = min_experience
        self.email = email

        def __repr__(self):
            return f'''{self.id}, {self.admin_id},{self.role}, {self.company}, {self.location}, {self.responsibilities}, {self.requirements}, {self.website}, {self.salary}',
            {self.currency},{self.min_experience},{self.email}'''