from sqlalchemy import Column, Integer, String
from app.database import Base

class Customer(Base):

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    address = Column(String)