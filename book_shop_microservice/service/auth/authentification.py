from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from book_shop_microservice.core.database import get_db
from book_shop_microservice.service.user import get_user_by_user_for_auth

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/token")

def veryfy_user_for_router(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentails_exeption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="It's mistake"
    )
    try:
        payload: dict = jwt.decode(
            token, "secret_key", algorithms=["HS256"]
        )
        username: str = payload.get("sub")
        if not username:
            raise credentails_exeption
    except JWTError:
        raise credentails_exeption
    user = get_user_by_user_for_auth(username, db)
    if not user:
        raise credentails_exeption
    return True