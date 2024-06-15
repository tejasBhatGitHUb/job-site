from schemas import schemas
from database.queries import client
from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import jose

router = APIRouter(
    tags=["Authentication"]
)


@router.post('/signup', response_model=schemas.ShowUserInput)
def signup(request: schemas.UserInput):
    # try:
    client.signup(request)
    return request
    # except:
    #     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User already exists.")


@router.post('/login')
def login(request: schemas.Signin):
    try:
        name =client.signin(request)
        return f"Welcome back {name} "
    except NameError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No user Found ")
    except:
        return "Wrong password"
