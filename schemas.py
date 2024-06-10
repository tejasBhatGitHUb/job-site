from pydantic import BaseModel


class ShowSignup(BaseModel):
    full_name: str
    highest_education: str
    years_of_experience: float
    skills: str
    linkedin_url: str
    resume_url: str

    class Config:
        orm_mode = True


class Signup(ShowSignup):
    status: str
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str


class UpdateUser(BaseModel):
    highest_education: str
    years_of_experience: float
    skills: str
    linkedin_url: str
    resume_url: str
    password: str

    class Config:
        orm_mode = True


class ShowUpdateUser(UpdateUser):
    pass


class ShowJobs(BaseModel):
    id: int
    role: str
    company: str
    salary: int
    currency: str
    min_experience: float

    class Config:
        orm_model = True


class ShowJob(ShowJobs):
    location: str
    responsibilities: str
    requirements: str
    website: str


class ShowApplication(ShowSignup):
    job_id: int


class DeleteApplication(BaseModel):
    job_id: int


class ShowUser(ShowSignup):
    pass


class PostJob(BaseModel):
    role: str
    location: str
    responsibilities: str
    requirements: str
    website: str
    company: str
    salary: int
    currency: str
    min_experience: float
    email: str


class ShowPostedJob(PostJob):
    pass
