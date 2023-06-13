from datetime import timedelta, datetime

from jose import jwt
from sqlalchemy.orm import Session
from typing import Optional

from book_shop_microservice.models import User
from book_shop_microservice.schemes.user import UserCreate
from book_shop_microservice.service.hashing import Hasher


def create_new_user(user:UserCreate,db: Session):
    db_user = User(
        username=user.username,
        name=user.name,
        surname=user.surname,
        email=user.email,
        password=Hasher.get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {'register succses':
                {'username':user.username,
                 'email': user.email}
            }

def autheficate_user(username: str, password: str, db: Session):
    user = get_user_by_user_for_auth(username, db)
    if not user:
        return {'massage': "user not exists"}
    if not Hasher.veryfy_password(password, user.password):
        return {'massage': "password isn\'t right"}
    return user


def get_user_by_user_for_auth(username: str, db: Session):
    query_username = db.query(User).where(User.username==username).one()
    return query_username

def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, "secret_key", "HS256")
    return encode_jwt