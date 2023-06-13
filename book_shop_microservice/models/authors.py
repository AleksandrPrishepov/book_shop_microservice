from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base
from .many_to_many_models import book_author


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    author_name = Column(String, nullable=False)
    book_for_mtm = relationship("Book", secondary=book_author,
                                  back_populates="author", lazy=True)

    book = relationship("Book", back_populates="author")

