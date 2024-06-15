from typing import List
from schemas import schemas
from database.queries import recruiters
from fastapi import APIRouter, HTTPException, status, Path

router = APIRouter(
    tags=["Recruiter"]
)


@router.get('/recruiter/{id}/profile', response_model=schemas.ShowRecruiterProfile)
def show_recruiter(id: int = Path(..., description="User ID", gt=0)):
    try:
        user = recruiters.show_profile(id)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")


@router.get('/recruiter/{id}/profile/update', response_model=schemas.ShowRecruiterInput)
def update_recruiter(id: int, request: schemas.UpdateRecruiter):
    recruiters.update_profile(id, request)
    return recruiters.show_profile(id)


@router.post('/recruiter/{id}/post', response_model=schemas.ShowJobsInput)
def post_job(request: schemas.JobsInput, id: int = Path(..., description="User ID", gt=0)):
    # try:
    recruiters.post_job(id, request)
    return request
    # except RuntimeError:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You are not allowed to post a job opening")
    # except:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Job already exists.")


@router.get('/recruiter/{id}/posted', response_model=List[schemas.ShowJobs])
def posted_jobs(id: int = Path(..., description="User ID", gt=0)):
    try:
        return recruiters.my_postings(id)
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not allowed")


@router.get('/recruiter/{id}/posted/{job_id}/applications', response_model=List[schemas.ShowUserInput])
def received_applications(id: int = Path(..., description="User ID", gt=0),
                          job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        return recruiters.received_applications(id, job_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Method not allowed")


@router.delete('/recruiter/{id}/posted/delete/{job_id}')
def delete_job(id: int = Path(..., description="User ID", gt=0), job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        recruiters.delete_job(id, job_id)
        return f"Deleted job with id {job_id}"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Your not allowed to delete the job openings")
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="something went wrong")
