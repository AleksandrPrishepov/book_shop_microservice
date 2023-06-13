from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class ShopQuantity(Base):
    __tablename__ = "shopquantity"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=0)

    book = relationship("Book", back_populates="shopquantity")