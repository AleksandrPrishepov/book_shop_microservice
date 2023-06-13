from pydantic import BaseModel, EmailStr
import uuid

class UserCreate(BaseModel):
    id: uuid.UUID
    username: str
    name: str
    surname: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str