from schemas import schemas
from database import queries
from fastapi import APIRouter, HTTPException, status, Path

router = APIRouter(
    tags=["Authentication"]
)


@router.post('/signup', response_model=schemas.ShowSignup)
def signup(request: schemas.Signup):
    try:
        queries.add_user(request)
        return request
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User already exists.")


@router.post('/login')
def login(request: schemas.Login):
    try:
        name = queries.check_credentials(request)
        return f"Welcome back {name} "
    except NameError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")
    except:
        return "Wrong password"
