from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    author_name = Column(String, nullable=False)

    book = relationship("Book", back_populates="author")



# class Book(Base):
#     __tablename__ = "book"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     price = Column(Numeric)
#     author_id = Column(Integer, ForeignKey("author.id"))
#     genre_id = Column(Integer, ForeignKey("genre.id"))
#
#     check = relationship("Check", back_populates="book")
#     author = relationship("Author", back_populates="book")
#     genre = relationship("Genre", back_populates="book")

# class Genre(Base):
#     __tablename__ = "genre"
#
#     id = Column(Integer, primary_key=True)
#     genre_name = Column(String, nullable=False)
#
#     book = relationship("Book", back_populates="genre")

# class Salesman(Base):
#     __tablename__ = "salesman"
#
#     id = Column(Integer, primary_key=True)
#     salesman_name = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)
#
#     order = relationship("Order", back_populates="salesman")

# class Order(Base):
#     __tablename__ = "order"
#
#     id = Column(Integer, primary_key=True)
#     check_id = Column(Integer, ForeignKey("check.id"))
#     buyer_id = Column(Integer, ForeignKey("buyer.id"))
#     salesman_id = Column(Integer, ForeignKey("salesman.id"))
#
#     check = relationship("Check", back_populates="order")
#     buyer = relationship("Buyer", back_populates="order")
#     salesman = relationship("Salesman", back_populates="order")

# class Check(Base):
#     __tablename__ = "check"
#
#     id = Column(Integer, primary_key=True)
#     book_id = Column(Integer, ForeignKey("book.id"))
#     count = Column(Integer)
#
#     order = relationship("Order", back_populates="check")
#     book = relationship("Book", back_populates="check")

# class Buyer(Base):
#     __tablename__ = "buyer"
#
#     id = Column(Integer, primary_key=True)
#     buyer_name = Column(String, nullable=False)
#     city = Column(String, nullable=False)
#
#     order = relationship("Order", back_populates="buyer")