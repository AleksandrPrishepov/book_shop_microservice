from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.user import UserCreate
from book_shop_microservice.service.user import create_new_user, autheficate_user, create_access_token

router_auth = APIRouter(prefix='/auth',tags=['AUTHORIZATION'])

@router_auth.post('/register')
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    return create_new_user(user, db)

@router_auth.post('/login/token')
def login_for_access_token(form_data: OAuth2PasswordRequestForm=Depends(),
                           db: Session=Depends(get_db)
                           ):
    user = autheficate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='user not exists'
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token({"sub": user.username, "custom_date": [1,2,3]},
                                       expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}