from book_shop_microservice.models import Book
from book_shop_microservice.schemes.sheme import BookValidator


def post_book(book: BookValidator, db):
    db_book = Book(
        title=book.title,
        price=book.price,
        author_id=book.author_id,
        genre_id=book.genre_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book