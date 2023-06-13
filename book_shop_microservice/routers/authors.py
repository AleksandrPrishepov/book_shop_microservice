from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import AuthorValidator
from book_shop_microservice.service import authors

router_author = APIRouter(prefix="/author", tags=["AUTHOR"])


@router_author.post("/create")
def post_author(author: AuthorValidator, session: Session = Depends(get_db)):
    return authors.post_author(author, session)


@router_author.get("/list")
def get_author(id: Optional[int] = None, session: Session = Depends(get_db)):
    return authors.get_author(id, session)


@router_author.get("/author/book")
def get_author_and_book(session: Session = Depends(get_db)):
    return authors.get_author_and_book(session)



