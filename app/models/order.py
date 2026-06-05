# Order model
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column (
    Integer,
    primary_key=True,
    index=True
    )
    
    customer_id = Column(
    Integer,
    ForeignKey("customers.id"),
    index=True
    )

    product_id = Column(
    Integer,
    ForeignKey("products.id"),
    index=True
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )