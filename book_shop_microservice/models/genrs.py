from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base
from book_shop_microservice.models.many_to_many_models import book_genre


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    genre_name = Column(String, nullable=False)
    book_for_mtm = relationship("Book", secondary=book_genre,
                                back_populates="genre", lazy=True)

    book = relationship("Book", back_populates="genre")
