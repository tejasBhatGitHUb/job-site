from typing import List
from schemas import schemas
from database.queries import users
from fastapi import APIRouter, HTTPException, status, Path

router = APIRouter(
    tags=["User"]
)


# @router.get('/user', response_model=List[schemas.ShowAllUsers])
# def get_all_users():
#     return queries.get_users()


@router.get('/user/{id}/profile', response_model=schemas.ShowUserProfile)
def show_profile(id: int = Path(..., description="User ID", gt=0)):
    try:
        user = users.show_profile(id)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="We encountered an issue while serving your request pleases try again")


@router.patch('/user/{id}/profile/update', response_model=schemas.ShowUserInput)
def update_profile(request: schemas.UpdateUser, id: int = Path(..., description="User ID", gt=0)):
    try:
        print(request)
        users.update_profile(id,request)
        return users.show_profile(id)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@router.delete('/user/{id}/profile/delete')
def delete_account(id: int = Path(..., description="User ID", gt=0)):
    try:
        users.delete_profile(id)
        return "Profile Deleted Successfully"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="You are not allowed to delete your account as an admin")
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.get('/user/{id}/profile/applications', response_model=List[schemas.ShowJobs])
def show_my_applications(id: int = Path(..., description="User ID", gt=0)):
    return users.my_applications(id)


@router.delete('/user/{id}/profile/applications/delete/{job_id}')
def delete_my_application(id: int = Path(..., description="User ID", gt=0),
                          job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        users.delete_application(id, job_id)
        return f"Deleted your application for job id {job_id}"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="")
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something went wrong")


@router.get('/user/{id}/jobs', response_model=List[schemas.ShowJobs])
def show_all_jobs():
    try:
        return users.get_all_jobs()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="We encountered an issue while serving your request pleases try again")


@router.get('/user/{id}/jobs/{job_id}', response_model=schemas.ShowJobsInput)
def job_details(job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        return users.get_job(job_id)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Sorry this job opening is not present in our Database")


@router.post('/user/{id}/jobs/{job_id}/apply')
def apply(id: int = Path(..., description="User ID", gt=0), job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        users.apply(id, job_id)
        return "Applied"
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="You already applied for this job or the job opening is no longer available for you")
