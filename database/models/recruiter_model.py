from sqlalchemy import Column, INTEGER, VARCHAR, DateTime, func, create_engine
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()
Base = declarative_base()


class Recruiter(Base):
    __tablename__ = 'recruiters'
    id = Column('id', INTEGER, autoincrement=True, primary_key=True)
    status = Column("status", VARCHAR(10), default="user")
    hr_name = Column('hr_name', VARCHAR(100))
    hr_email = Column("email", VARCHAR(50))
    company_name = Column('company_name', VARCHAR(150), unique=True)
    company_address = Column("company_address", VARCHAR(1000))
    company_email = Column("company_email", VARCHAR(50), unique=True)
    company_registered_phone_number = Column("company_registered_phone_number", VARCHAR(10), unique=True)
    secondary_phone_number = Column("secondary_phone_number", VARCHAR(10))
    company_linkedin_url = Column('linkedin_url', VARCHAR(100), unique=True)
    password = Column('password', VARCHAR(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, hr_name, status, hr_email, company_name, company_address, company_email, company_linkedin_url,
                 company_registered_phone_number, secondary_phone_number, password):
        self.hr_name = hr_name
        self.status = status
        self.hr_email = hr_email
        self.company_name = company_name
        self.company_address = company_address
        self.company_email = company_email
        self.company_linkedin_url = company_linkedin_url
        self.company_registered_phone_number = company_registered_phone_number
        self.secondary_phone_number = secondary_phone_number
        self.password = password

    # def __repr__(self):
    #     return f'''{self.id}, {self.full_name}, {self.status},{self.email}, {self.skills}, {self.resume_url}, {self.linkedin_url}, {self.years_of_experience}, {self.highest_education}'''


engine = create_engine(os.getenv("connection_string"))
Base.metadata.create_all(bind=engine)