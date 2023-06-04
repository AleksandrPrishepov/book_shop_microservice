from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    check_id = Column(Integer, ForeignKey("check.id"))
    buyer_id = Column(Integer, ForeignKey("buyer.id"))
    salesman_id = Column(Integer, ForeignKey("salesman.id"))

    check = relationship("Check", back_populates="order")
    buyer = relationship("Buyer", back_populates="order")
    salesman = relationship("Salesman", back_populates="order")
