from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    genre_name = Column(String, nullable=False)

    book = relationship("Book", back_populates="genre")
