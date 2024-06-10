from os import getenv
from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, INTEGER, VARCHAR, FLOAT, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()
load_dotenv()


class JobApplication(Base):
    __tablename__ = "job_applications"
    job_id = Column('job_id', INTEGER, ForeignKey('jobs.id'), primary_key=True)
    user_id = Column('user_id', INTEGER, ForeignKey('users.id'), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    applicants = relationship("Job", backref='applicants')
    applied = relationship("User", backref="applied")


class User(Base):
    __tablename__ = 'users'
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    status = Column("status", VARCHAR(5),default="user")
    full_name = Column('full_name', VARCHAR(100))
    email = Column("email", VARCHAR(100))
    highest_education = Column('highest_education', VARCHAR(50))
    years_of_experience = Column('years_of_experience', FLOAT)
    skills = Column('skills', VARCHAR(1000))
    linkedin_url = Column('linkedin_url', VARCHAR(100))
    resume_url = Column('resume_url', VARCHAR(500))
    password = Column('password', VARCHAR(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


    def __init__(self, full_name,status,email, highest_education, years_of_experience, skills, linkedin_url,
                 resume_url, password):
        self.full_name = full_name
        self.status=status
        self.email = email
        self.highest_education = highest_education
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.linkedin_url = linkedin_url
        self.resume_url = resume_url
        self.password = password

    def __repr__(self):
        return f'''{self.id}, {self.full_name}, {self.status},{self.email}, {self.skills}, {self.resume_url}, {self.linkedin_url}, {self.years_of_experience}, {self.highest_education}'''


class Job(Base):
    __tablename__ = "jobs"
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    admin_id=Column('admin_id', INTEGER)
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


    def __init__(self,admin_id, role, company, location, responsibilities, requirements, website, salary, currency,
                 min_experience,
                 email):
        self.admin_id=admin_id
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
def initialize_db():
    engine = create_engine(getenv("connection_string"))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
