from  pydantic import BaseModel
import uuid


class BuyerVaidator(BaseModel):
    id: uuid.UUID
    buyer_name: str
    city: str

class AuthorValidator(BaseModel):
    id: uuid.UUID
    author_name: str

class SalesmanValidator(BaseModel):
    id: uuid.UUID
    salesman_name: str
    age: int

class GenreValidator(BaseModel):
    id: uuid.UUID
    genre_name: str

class BookValidator(BaseModel):
    id: uuid.UUID
    title: str
    price: float
    author_id: int
    genre_id: int


