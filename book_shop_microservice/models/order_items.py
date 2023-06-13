from sqlalchemy import Column, ForeignKey, Integer, Numeric, DateTime
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class OrderItems(Base):
    __tablename__ = "orderitems"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    price = Column(Numeric)
    cost = Column(Numeric)
    create_at = Column(DateTime)
    book_id = Column(Integer, ForeignKey("book.id"))
    salesman_id = Column(Integer, ForeignKey("salesman.id"))
    order_id = Column(Integer, ForeignKey("order.id"))

    book = relationship("Book", back_populates="orderitems")
    salesman = relationship("Salesman", back_populates="orderitems")
    order = relationship("Order", back_populates="orderitems")


