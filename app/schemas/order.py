from pydantic import BaseModel


class OrderCreate(BaseModel):

    customer_id: int

    product_id: int

    quantity: int


class OrderUpdate(BaseModel):

    customer_id: int | None = None

    quantity: int | None = None


class OrderResponse(BaseModel):

    id: int

    customer_id: int

    product_id: int

    quantity: int

    total_amount: float

    class Config:
        from_attributes = True