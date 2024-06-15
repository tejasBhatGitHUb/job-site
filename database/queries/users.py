from sqlalchemy import and_
from database.initialize_database_models import initialize_db
from database.models.user_model import User
from database.models.job_model import Job
from database.models.job_application_model import JobApplication

session = initialize_db()

def delete_profile(id: int):
    user = session.query(User).filter(User.id == id)
    if not user.first():
        raise Exception("User not Found")
    session.query(JobApplication).filter(
        JobApplication.user_id == id).delete()
    user.delete()
    session.commit()


def show_profile(id):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        return Exception("User not found")
    return user


# def get_users():
#     return session.query(User).all()


def update_profile(id, request):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        return Exception("User not found")
    for key, val in request.dict().items():
        if val!=None:
            setattr(user, key, val)
    session.commit()


#not unique
def update_password(id, request):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        raise Exception("User not found")
    if user.password!=request.old_password:
        raise Exception("Wrong password")
    user.password = request.password
    session.commit()


def get_all_jobs():
    jobs = session.query(Job).all()
    return jobs


# user
def get_job(id):
    return session.query(Job).filter(Job.id == id).first()


def apply(user_id, job_id):
    try:
        # if session.query(User.status).filter(User.id == user_id).first()[0] == "admin":
        #     raise Exception
        application = JobApplication(job_id=job_id, user_id=user_id)
        session.add(application)
        session.commit()
    except:
        session.close()
        raise Exception


# user
def delete_application(user_id, job_id):
    application = session.query(JobApplication).filter(
        and_(JobApplication.user_id == user_id, JobApplication.job_id == job_id))
    if not application.first():
        raise Exception
    application.delete()
    session.commit()


# user
def my_applications(id: int):
    return session.query(Job).filter(JobApplication.user_id==id).filter(Job.id==JobApplication.job_id).all()

