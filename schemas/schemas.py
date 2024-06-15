from typing import Optional

from pydantic import BaseModel,EmailStr


class Signin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class ShowUserInput(BaseModel):
    full_name: str
    email: EmailStr
    highest_education: str
    years_of_experience: float
    skills: str
    linkedin_url: str
    resume_url: str

    class Config:
        orm_mode = True


class UserInput(BaseModel):
    status: str
    full_name: str
    email: EmailStr
    highest_education: str
    years_of_experience: float
    skills: str
    linkedin_url: str
    resume_url: str
    password: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    highest_education: Optional[str]=None
    years_of_experience: Optional[float]=None
    skills: Optional[str]=None
    linkedin_url: Optional[str]=None
    resume_url: Optional[str]=None

    class Config:
        orm_mode = True


class ShowUpdateUser(ShowUserInput):
    pass


class ShowRecruiterInput(BaseModel):
    id: int
    hr_name: str
    hr_email: EmailStr
    company_name: str
    company_address: str
    company_email: EmailStr
    company_linkedin_url: str

    class Config:
        orm_mode = True


class RecruiterInput(ShowRecruiterInput):
    status: str
    hr_name: str
    hr_email: EmailStr
    company_name: str
    company_address: str
    company_email: EmailStr
    company_linkedin_url: str
    company_registered_phone_number: str
    secondary_phone_number: str
    password: str


class ShowUpdateRecruiter(ShowRecruiterInput):
    pass


class UpdateRecruiter(BaseModel):
    hr_name: Optional[str]=None
    hr_email:Optional[EmailStr]=None
    company_address: Optional[str]=None
    secondary_phone_number: Optional[str]=None

    class Config:
        orm_mode = True


class ShowJobsInput(BaseModel):
    id: str
    role: str
    company: str
    location: str
    responsibilities: str
    requirements: str
    website: str
    salary: int
    min_experience: float
    perks: str
    email: EmailStr

    class Config:
        orm_mode = True


class JobsInput(BaseModel):
    recruiter_id: int
    role: str
    company: str
    location: str
    responsibilities: str
    requirements: str
    website: str
    salary: int
    min_experience: float
    perks: str
    email: EmailStr

    class Config:
        orm_mode = True


class ShowJobs(BaseModel):
    id: int
    role: str
    company: str
    location: str
    salary: int
    min_experience: float

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str

    class Config:
        orm_mode = True


class ShowUserProfile(ShowUserInput):
    id: int


class ShowRecruiterProfile(ShowRecruiterInput):
    id: int
