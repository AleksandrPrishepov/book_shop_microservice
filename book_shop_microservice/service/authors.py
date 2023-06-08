from typing import Optional

from book_shop_microservice.models import Author, Book
from book_shop_microservice.schemes.sheme import AuthorValidator


def post_author(author: AuthorValidator, db):
    db_author = Author(author_name=author.author_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_author(id: Optional[int], db):
    if id == None:
        return db.query(Author).order_by(Author.author_name).all()
        # my_select = select(Author)
        # return session.execute(my_select).all()

    else:
        return db.query(Author).filter(Author.id == id).one()
        # my_select = select(Author).where(Author.id == id)
        # return session.execute(my_select).all()

def get_author_and_book(db):
    return db.query(Author.author_name, Book.title).filter(
        Author.id == Book.author_id
    )
    # return session.query(Author).join(Book).filter(Author.id > 2).one()
