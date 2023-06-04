from fastapi import APIRouter
from sqlalchemy import and_
from typing import Optional
from book_shop_microservice.models import Genre, Book
from book_shop_microservice.models.authors import Author
from book_shop_microservice.models.buyer import Buyer
from book_shop_microservice.models.salesmen import Salesman
from book_shop_microservice.schemes.sheme import BuyerVaidator, AuthorValidator, SalesmanValidator, GenreValidator, \
    BookValidator

from book_shop_microservice.core.database import SessionLocal


router_buyer = APIRouter()

@router_buyer.post("/create")
def post_buyer(buyer: BuyerVaidator):
    with SessionLocal() as session:
        db_buyer = Buyer(
            buyer_name=buyer.buyer_name,
            city=buyer.city
        )
    session.add(db_buyer)
    session.commit()
    session.refresh(db_buyer)
    return db_buyer
@router_buyer.get("/list/{id}")
def get_buyer(id: int):
    with SessionLocal() as session:
        res = session.query(Buyer).filter(and_(Buyer.id > id, Buyer.city.like('Ми%'))).one_or_none()
    return res


router_author = APIRouter()

@router_author.post("/create")
def post_author(author: AuthorValidator):
    with SessionLocal() as session:
        db_author = Author(
            author_name=author.author_name,
        )
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author

@router_author.get("/list")
def get_author(id: Optional[int] = None):
    with SessionLocal() as session:
        if id == None:
            return session.query(Author).order_by(Author.author_name).all()
        else:
            return session.query(Author).filter(Author.id == id).all()

@router_author.get("/author/book")
def get_author_and_book():
    with SessionLocal() as session:
        return session.query(Author.author_name, Book.title).filter(Author.id == Book.author_id)
        # return session.query(Author).join(Book).filter(Author.id > 2).one()




router_salesman = APIRouter()

@router_salesman.post("/create")
def post_salesman(salesman: SalesmanValidator):
    with SessionLocal() as session:
        db_salesman = Salesman(
            salesman_name=salesman.salesman_name,
            age=salesman.age
        )
        # db_salesman = Salesman(salesman.dict())
    session.add(db_salesman)
    session.commit()
    session.refresh(db_salesman)
    return db_salesman

router_genre = APIRouter()

@router_genre.post("/create")
def post_genre(genre: GenreValidator):
    with SessionLocal() as session:
        db_genre = Genre(genre_name=genre.genre_name)
        session.add(db_genre)
        session.commit()
        session.refresh(db_genre)
    return db_genre

router_book = APIRouter()

@router_book.post("/create")
def post_book(book: BookValidator):
    with SessionLocal() as session:
        db_book = Book(
            title=book.title,
            price=book.price,
            author_id=book.author_id,
            genre_id=book.genre_id
        )
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
    return db_book


main_router_api = APIRouter()
main_router_api.include_router(router_buyer, prefix="/buyer", tags=["BUYER"])
main_router_api.include_router(router_author, prefix="/author", tags=["AUTHOR"])
main_router_api.include_router(router_salesman, prefix="/salesman", tags=["SALESMAN"])
main_router_api.include_router(router_genre, prefix="/genre", tags=["GENRE"])
main_router_api.include_router(router_book, prefix="/book", tags=["BOOK"])