from typing import List
from schemas import schemas
from database import queries
from fastapi import APIRouter, HTTPException, status, Path

router = APIRouter(
    tags=["Admin"]
)


@router.get('/admin/{id}', response_model=schemas.ShowUser)
def show_user(id: int = Path(..., description="User ID", gt=0)):
    try:
        user = queries.get_user(id)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")


@router.post('/admin/{id}/post', response_model=schemas.ShowPostedJob)
def post_job(response: schemas.PostJob, id: int = Path(..., description="User ID", gt=0)):
    try:
        print(queries.add_job(id, response))
        return response
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You are not allowed to post a job opening")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Job already exists.")


@router.get('/admin/{id}/posted', response_model=List[schemas.ShowJob])
def posted_jobs(id: int = Path(..., description="User ID", gt=0)):
    try:
        return queries.my_postings(id)
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not allowed")


@router.get('/admin/{id}/posted/{job_id}/applications', response_model=List[schemas.ReceivedApplications])
def received_applications(id: int = Path(..., description="User ID", gt=0),
                          job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        return queries.received_applications(id, job_id)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Method not allowed")


@router.delete('/admin/{id}/posted/delete/{job_id}')
def delete_job(id: int = Path(..., description="User ID", gt=0), job_id: int = Path(..., description="Job ID", gt=0)):
    try:
        queries.delete_job(id, job_id)
        return f"Deleted job with id {job_id}"
    except RuntimeError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Your not allowed to delete the job openings")
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="something went wrong")
