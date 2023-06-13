from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String, Text
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base
from .many_to_many_models import book_author, book_genre


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    discription =Column(Text, default=None)
    image = Column(LargeBinary, default=False)
    publishing_id = Column(Integer, ForeignKey("publishing.id"))
    author_id = Column(Integer, ForeignKey("author.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))
    shop_quantity_id = Column(Integer, ForeignKey("shopquantity.id"))
    author_for_mtm = relationship("Author", secondary=book_author,
                                  back_populates="book", lazy=True)
    genre_for_mtm = relationship("Genre", secondary=book_genre,
                                  back_populates="book", lazy=True)

    publishing = relationship("Publishing", back_populates="book")
    order_items = relationship("OrderItems", back_populates="book")
    author = relationship("Author", back_populates="book")
    genre = relationship("Genre", back_populates="book")
    shop_quantity = relationship("ShopQuantity", back_populates="book")

