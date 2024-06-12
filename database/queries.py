from sqlalchemy import and_
from .initialize_database_models import initialize_db
from .models.user_model import User
from .models.job_model import Job
from .models.job_application_model import JobApplication

session = initialize_db()


def add_user(request):
    if session.query(User.email).filter(User.email == request.email).first():
        raise Exception
    user = User(full_name=request.full_name, highest_education=request.highest_education,
                email=request.email, years_of_experience=request.years_of_experience,
                skills=request.skills, linkedin_url=request.linkedin_url,
                resume_url=request.resume_url, password=request.password, status=request.status)
    session.add(user)
    session.commit()


def delete_user(id: int):
    user = session.query(User).filter(User.id == id)
    if not user.first():
        raise Exception
    if user.first().status == "admin":
        raise RuntimeError
    session.query(JobApplication).filter(
        JobApplication.user_id == id).delete()
    user.delete()
    session.commit()


def get_user(id):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        return Exception
    return user


def get_users():
    return session.query(User).all()


def update_user_profile(id, request):
    user = session.query(User).filter(User.id == id).first()
    user.highest_education = request.highest_education
    user.years_of_experience = request.years_of_experience
    user.skills = request.skills
    user.linkedin_url = request.linkedin_url
    user.resume_url = request.resume_url
    user.password = request.password
    session.commit()


def add_job(id: int, request):
    if session.query(Job.admin_id, Job.role, Job.min_experience).filter(
            and_(Job.admin_id == id, Job.role == request.role, Job.min_experience == request.min_experience)).first():
        raise Exception
    if session.query(User.status).filter(User.id == id).first()[0] == "user":
        raise RuntimeError
    job = Job(role=request.role, company=request.company, location=request.location,
              responsibilities=request.responsibilities,
              requirements=request.requirements, website=request.website, salary=request.salary,
              currency=request.currency,
              min_experience=request.min_experience, email=request.email, admin_id=id)
    session.add(job)
    session.commit()


def get_all_jobs():
    jobs = session.query(Job).all()
    return jobs


def get_job(id):
    return session.query(Job).filter(Job.id == id).first()


def delete_job(id, job_id):
    if session.query(User.status).filter(User.id == id).first()[0] == "user":
        raise RuntimeError
    job = session.query(Job).filter(and_(Job.id == job_id, Job.admin_id == id))
    if not job.first():
        raise Exception
    session.query(JobApplication).filter(
        JobApplication.job_id == job_id).delete()
    job.delete()
    session.commit()


def apply(user_id, job_id):
    try:
        if session.query(User.status).filter(User.id == user_id).first()[0] == "admin":
            raise Exception
        application = JobApplication(job_id=job_id, user_id=user_id)
        session.add(application)
        session.commit()
    except:
        session.close()
        raise Exception


def delete_application(user_id, job_id):
    application = session.query(JobApplication).filter(
        and_(JobApplication.user_id == user_id, JobApplication.job_id == job_id))
    if not application.first():
        raise Exception
    application.delete()
    session.commit()


def my_applications(id: int):
    user = session.query(User).filter(User.id == id).first()
    return [session.query(Job).filter(Job.id == application.job_id).first() for application in user.applied]


def received_applications(id: int, job_id: int):
    if session.query(User.status).filter(User.id == id).first()[0] == "user":
        raise RuntimeError
    if session.query(Job.admin_id).filter(Job.id == job_id).first()[0] != id:
        raise Exception
    applicants = session.query(JobApplication).filter(JobApplication.job_id == job_id).all()
    return [session.query(User).filter(User.id == applicant.user_id).first() for applicant in applicants]


def my_postings(id: int):
    if session.query(User.status).filter(User.id == id).first()[0] == "user":
        raise RuntimeError
    return session.query(Job).filter(Job.admin_id == id).all()


def check_credentials(request):
    has_user = session.query(User).filter(User.email == request.email).first()
    print(has_user)
    if not has_user:
        raise NameError
    user = session.query(User).filter(
        and_(User.email == request.email, User.password == request.password)).first()
    print(user)
    if not user:
        raise Exception
    return user.full_name
