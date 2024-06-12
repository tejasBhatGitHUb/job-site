from typing import List

from fastapi import FastAPI, HTTPException, status
import uvicorn
import schemas
import queries

app = FastAPI()


@app.get('/', tags=["Index"])
def index():
    return {"message":"WELCOME!!!"}


@app.post('/signup', response_model=schemas.ShowSignup, tags=["Authentication"])
def signup(request: schemas.Signup):
    try:
        queries.add_user(request)
        return request
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User already exists.")


@app.post('/login', tags=["Authentication"])
def login(request: schemas.Login):
    try:
        name = queries.check_crentials(request)
        return f"Welcome back {name} "
    except NameError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")
    except:
        return "Wrong password"


@app.get('/user',response_model=List[schemas.ShowAllUsers],tags=["User"])
def get_all_users():
    return queries.get_users()

@app.get('/user/{id}/profile', response_model=schemas.ShowUser, tags=["User"])
def show_profile(id: int):
    try:
        user = queries.get_user(id)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="We encountered an issue while serving your request pleases try again")


@app.patch('/user/{id}/profile/update', response_model=schemas.UpdateUser, tags=["User"])
def update_profile(id: int, request: schemas.UpdateUser):
    try:
        queries.update_user_profile(id, request)
        return request
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@app.delete('/user/{id}/profile/delete', tags=["User"])
def delete_account(id: int):
    try:
        queries.delete_user(id)
        return "Profile Deleted Successfully"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="You are not allowed to delete your account as an admin")
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.get('/user/{id}/profile/applications', response_model=List[schemas.ShowJobs], tags=["User"])
def show_my_applications(id: int):
    return queries.my_applications(id)

@app.delete('/user/{id}/profile/applications/delete/{job_id}', tags=["User"])
def delete_my_application(id: int, job_id: int):
    try:
        queries.delete_application(id, job_id)
        return f"Deleted your application for job id {job_id} "
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@app.get('/user/{id}/jobs', response_model=List[schemas.ShowJobs], tags=["User"])
def show_all_jobs():
    try:
        return queries.get_all_jobs()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="We encountered an issue while serving your request pleases try again")


@app.get('/user/{id}/jobs/{job_id}', response_model=schemas.ShowJob, tags=["User"])
def job_details(job_id: int):
    try:
        return queries.get_job(job_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Sorry this job opening is not present in our Database")


@app.post('/user/{id}/jobs/{job_id}/apply', tags=["User"])
def apply(id: int, job_id: int):
    try:
        queries.apply(id, job_id)
        return "Applied"
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="You already applied for this job or the job opening is no longer available for you")


@app.get('/admin/{id}', response_model=schemas.ShowUser, tags=["Admin"])
def show_user(id: int):
    try:
        user = queries.get_user(id)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")


@app.post('/admin/{id}/post', response_model=schemas.ShowPostedJob, tags=["Admin"])
def post_job(id: int, response: schemas.PostJob):
    try:
        print(queries.add_job(id, response))
        return response
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="You are not allowed to post a job opening")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Job already exists.")


@app.get('/admin/{id}/posted', response_model=List[schemas.ShowJob], tags=["Admin"])
def posted_jobs(id: int):
    try:
        return queries.my_postings(id)
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Not allowed")


@app.get('/admin/{id}/posted/{job_id}/applications', response_model=List[schemas.ReceivedApplications], tags=["Admin"])
def received_applications(id: int, job_id: int):
    try:
        return queries.received_applications(id, job_id)
    except :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Method not allowed")



@app.delete('/admin/{id}/posted/delete/{job_id}', tags=["Admin"])
def delete_job(id:int,job_id: int):
    try:
        queries.delete_job(id,job_id)
        return f"Deleted job with id {job_id}"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Your not allowed to delete the job openings")
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="something went wrong")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
