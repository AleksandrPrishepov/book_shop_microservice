from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import BookValidator

router_book = APIRouter(prefix="/book", tags=["BOOK"])


@router_book.post("/create")
def post_book(book: BookValidator, session: Session = Depends(get_db)):
    return post_book(book, session)
