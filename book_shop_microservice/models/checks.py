from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Check(Base):
    __tablename__ = "check"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    count = Column(Integer)

    order = relationship("Order", back_populates="check")
    book = relationship("Book", back_populates="check")
