from sqlalchemy.orm import Session

from book_shop_microservice.models import Book
from book_shop_microservice.schemes.sheme import BookValidator


def post_book(book: BookValidator, db: Session):
    db_book = Book(
        title=book.title,
        author_id=book.author_id,
        genre_id=book.genre_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session, limit: int, offset: int):
    if limit == offset == None:
        return db.query(Book).all()
    if limit and offset:
        return db.query(Book).limit(limit).offset(offset).all()