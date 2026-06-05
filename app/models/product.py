# Product Model 
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Index

from app.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    sku = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    name = Column(
        String(255),
        nullable=False,
        index=True
    )

    price = Column(
        Float,
        nullable=False
    )

    stock = Column(
        Integer,
        default=0,
        nullable=False
    )

    __table_args__ = (
        Index("idx_product_name", "name"),
        Index("idx_product_sku", "sku"),
    )