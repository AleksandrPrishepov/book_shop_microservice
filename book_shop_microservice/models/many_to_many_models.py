from sqlalchemy import Column, ForeignKey, Integer, Numeric, Table
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


book_author = Table(
    'book_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('author_id', Integer, ForeignKey('author.id'))
)

book_genre = Table(
    'book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('book.id')),
    Column('genre_id', Integer, ForeignKey('genre.id'))
)