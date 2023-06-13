from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(Boolean, default=False)

    user = relationship("User", back_populates="order")
    order_item = relationship("OrderItems", back_populates="order")