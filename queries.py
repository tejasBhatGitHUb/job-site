from sqlalchemy import and_, or_
from database_models import Job, JobApplication, User, initialize_db

session = initialize_db()


def add_user(response):
    if session.query(User.email).filter(User.email == response.email).first():
        raise Exception
    user = User(full_name=response.full_name, highest_education=response.highest_education,
                email=response.email, years_of_experience=response.years_of_experience,
                skills=response.skills, linkedin_url=response.linkedin_url,
                resume_url=response.resume_url, password=response.password, status=response.status)
    session.add(user)
    session.commit()


def delete_user(id: int):
    user = session.query(User).filter(User.id == id)
    if not user.first():
        raise Exception
    if user.first().status=="admin":
        raise RuntimeError
    session.query(JobApplication).filter(JobApplication.user_id == id).delete()
    user.delete()
    session.commit()


def get_user(id):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        return Exception
    return user


def update_user_profile(id, response):
    user = session.query(User).filter(User.id == id).first()
    user.highest_education = response.highest_education
    user.years_of_experience = response.years_of_experience
    user.skills = response.skills
    user.linkedin_url = response.linkedin_url
    user.resume_url = response.resume_url
    user.password = response.password
    session.commit()


def add_job(id: int, response):
    if session.query(Job.admin_id, Job.role, Job.min_experience).filter(
            and_(Job.admin_id == id, Job.role == response.role, Job.min_experience == response.min_experience)).first():
        raise Exception
    job = Job(role=response.role, company=response.company, location=response.location,
              responsibilities=response.responsibilities,
              requirements=response.requirements, website=response.website, salary=response.salary,
              currency=response.currency,
              min_experience=response.min_experience, email=response.email, admin_id=id)
    session.add(job)
    session.commit()


def get_all_jobs():
    jobs = session.query(Job).all()
    return jobs


def get_job(id):
    return session.query(Job).filter(Job.id == id).first()


def delete_job(id):
    job = session.query(Job).filter(Job.id == id)
    if not job.first():
        raise Exception
    session.query(JobApplication).filter(JobApplication.job_id == id).delete()
    job.delete()
    session.commit()


def apply(user_id, job_id):
    try:
        if session.query(User.status).filter(User.id == 1).first()[0]=="admin":
            raise Exception
        application = JobApplication(job_id=job_id, user_id=user_id)
        session.add(application)
        session.commit()
    except:
        print('exception')
        session.refresh(User)
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
    applicants = session.query(JobApplication).filter(JobApplication.job_id == job_id).all()
    # return applicants
    return [session.query(User).filter(User.id == applicant.user_id).first() for applicant in applicants]


def my_postings(id: int):
    return session.query(Job).filter(Job.admin_id == id).all()


def check_crentials(request):
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

# print(session.query(User.status).filter(User.id==2).first()[0])