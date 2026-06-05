# Order schemas for request and response validation

from pydantic import BaseModel, Field

class OrderCreate(BaseModel):

    customer_id: int

    product_id: int

    quantity: int = Field(
        gt=0,
        description="Order quantity must be greater than 0"
    )

class OrderResponse(BaseModel):

    id: int

    customer_id: int

    product_id: int

    quantity: int

    total_amount: float

    class Config:
        from_attributes = True