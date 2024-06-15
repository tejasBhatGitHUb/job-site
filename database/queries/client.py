from sqlalchemy import and_
from database.initialize_database_models import initialize_db
from database.models.user_model import User
from database.models.recruiter_model import Recruiter

session = initialize_db()
def signin(request):
    has_user = session.query(User).filter(User.email == request.email).first()
    if not has_user:
        raise NameError
    user = session.query(User).filter(
        and_(User.email == request.email, User.password == request.password)).first()
    print(user)
    if not user:
        raise Exception
    return user.full_name

# exception
def signup(request):
    # try:
    if request.status=='user':
        user = User(full_name=request.full_name, highest_education=request.highest_education,
                    email=request.email, years_of_experience=request.years_of_experience,
                    skills=request.skills, linkedin_url=request.linkedin_url,
                    resume_url=request.resume_url, password=request.password, status=request.status)
        session.add(user)
    elif request.status=='recruiter':
        recruiter=Recruiter(hr_name=request.hr_name,status=request.status,hr_email=request.hr_email,
                            company_name=request.company_name,company_address=request.company_address,
                            company_linkedin_url=request.company_linkedin_url,company_registered_phone_number=request.company_registered_phone_number,
                            secondary_phone_number=request.secondary_phone_number,password=request.password)
        session.add(recruiter)
    # else:
    #     raise Exception("invalid status")
    session.commit()
    # except:
    #     session.close()
    #     raise Exception("user already exists in our database")