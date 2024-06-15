from dotenv import load_dotenv
from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
Base = declarative_base()
load_dotenv()



class User(Base):
    __tablename__ = 'users'
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    status = Column("status", VARCHAR(5), default="user")
    full_name = Column('full_name', VARCHAR(100))
    email = Column("email", VARCHAR(100),unique=True)
    highest_education = Column('highest_education', VARCHAR(50))
    years_of_experience = Column('years_of_experience', FLOAT)
    skills = Column('skills', VARCHAR(1000))
    linkedin_url = Column('linkedin_url', VARCHAR(100),unique=True)
    resume_url = Column('resume_url', VARCHAR(500),unique=True)
    password = Column('password', VARCHAR(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, full_name, status, email, highest_education, years_of_experience, skills, linkedin_url,
                 resume_url, password):
        self.full_name = full_name
        self.status = status
        self.email = email
        self.highest_education = highest_education
        self.years_of_experience = years_of_experience
        self.skills = skills
        self.linkedin_url = linkedin_url
        self.resume_url = resume_url
        self.password = password

    def __repr__(self):
        return f'''{self.id}, {self.full_name}, {self.status},{self.email}, {self.skills}, {self.resume_url}, {self.linkedin_url}, {self.years_of_experience}, {self.highest_education}'''


engine = create_engine(os.getenv("connection_string"))
Base.metadata.create_all(bind=engine)