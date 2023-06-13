from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Publishing(Base):
    __tablename__ = "publishing"

    id = Column(Integer, primary_key=True)
    publishing_name = Column(String, nullable=False)

    book = relationship("Book", back_populates="publishing")