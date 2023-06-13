from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import BookValidator
from book_shop_microservice.service.auth.authentification import veryfy_user_for_router
from book_shop_microservice.service.books import post_book, get_books

router_book = APIRouter(prefix="/book", tags=["BOOK"])


@router_book.post("/create")
def create_book(book: BookValidator, session: Session = Depends(get_db)):
    return post_book(book, session)

@router_book.get("/list")
def show_books(limit: int = None, offset: int=None,
               session: Session = Depends(get_db),
               access: bool = Depends(veryfy_user_for_router)):
    if access:
        return get_books(session, limit, offset)
