from sqlalchemy import String, Table, Column, Integer
from sqlalchemy.orm import relationship

from book_shop_microservice.core.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    order = relationship("Order", back_populates="user")
