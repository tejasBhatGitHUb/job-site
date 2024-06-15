from sqlalchemy import and_
from database.initialize_database_models import initialize_db
from database.models.user_model import User
from database.models.job_model import Job
from database.models.recruiter_model import Recruiter
from database.models.job_application_model import JobApplication

session = initialize_db()


# def delete_profile(id: int):
#     user = session.query(User).filter(User.id == id)
#     if not user.first():
#         raise Exception("User not Found")
#     session.query(JobApplication).filter(
#         JobApplication.user_id == id).delete()
#     user.delete()
#     session.commit()


def show_profile(id):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        return Exception("User not found")
    return user


# selected update
def update_profile(id, request):
    recruiter = session.query(Recruiter).filter(Recruiter.id == id).first()
    if not recruiter:
        return Exception("User not found")
    for key,val in request.dict().items():
        if val != None:
            setattr(recruiter,key,val)
    session.commit()


def update_password(id, request):
    recruiter = session.query(Recruiter).filter(Recruiter.id == id).first()
    if not recruiter:
        raise Exception("User not found")
    if recruiter.password!=request.old_password:
        raise Exception("Wrong password")
    recruiter.password = request.password
    session.commit()


# recruiter
# make changes
def post_job(id: int, request):
    if session.query(Job.recruiter_id, Job.role, Job.min_experience).filter(
            and_(Job.recruiter_id == id, Job.role == request.role, Job.min_experience == request.min_experience)).first():
        raise Exception("all ready exists")
    # if session.query(User.status).filter(User.id == id).first()[0] == "user":
    #     raise RuntimeError
    job = Job(role=request.role, company=request.company, location=request.location,
              responsibilities=request.responsibilities,
              requirements=request.requirements, website=request.website, salary=request.salary,
              min_experience=request.min_experience, email=request.email, recruiter_id=id,perks=request.perks)
    session.add(job)
    session.commit()


# jobs
def get_all_jobs():
    jobs = session.query(Job).all()
    return jobs


# user
# def get_job(id):
#     return session.query(Job).filter(Job.id == id).first()


# recruiter
# make changes
def delete_job(id, job_id):
    # if session.query(User.status).filter(User.id == id).first()[0] == "user":
    #     raise RuntimeError
    job = session.query(Job).filter(and_(Job.id == job_id, Job.recruiter_id == id))
    if not job.first():
        raise Exception
    session.query(JobApplication).filter(
        JobApplication.job_id == job_id).delete()
    job.delete()
    session.commit()


# recruiter
def received_applications(id: int, job_id: int):
    # if session.query(User.status).filter(User.id == id).first()[0] == "user":
    #     raise RuntimeError
    if session.query(Job.admin_id).filter(Job.id == job_id).first()[0] != id:
        raise Exception
    applicants = session.query(JobApplication).filter(JobApplication.job_id == job_id).all()
    return [session.query(User).filter(User.id == applicant.user_id).first() for applicant in applicants]


# recruiter
def my_postings(id: int):
    # if session.query(User.status).filter(User.id == id).first()[0] == "user":
    #     raise RuntimeError
    return session.query(Job).filter(Job.admin_id == id).all()
