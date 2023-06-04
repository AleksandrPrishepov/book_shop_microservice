from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Numeric)
    author_id = Column(Integer, ForeignKey("author.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))

    check = relationship("Check", back_populates="book")
    author = relationship("Author", back_populates="book")
    genre = relationship("Genre", back_populates="book")
