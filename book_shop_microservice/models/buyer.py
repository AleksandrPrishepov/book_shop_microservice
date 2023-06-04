from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base, SessionLocal as s



class Buyer(Base):
    __tablename__ = "buyer"

    id = Column(Integer, primary_key=True)
    buyer_name = Column(String, nullable=False)
    city = Column(String, nullable=False)

    order = relationship("Order", back_populates="buyer")

    def __repr__(self):
        return f"Buyer {self.buyer_name} из {self.city}"

