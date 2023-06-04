from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Salesman(Base):
    __tablename__ = "salesman"

    id = Column(Integer, primary_key=True)
    salesman_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="salesman")
