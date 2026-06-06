# Product schemas for request and response validation
from pydantic import BaseModel
from pydantic import Field


class ProductCreate(BaseModel):

    sku: str = Field(
        min_length=3,
        max_length=100
    )

    name: str = Field(
        min_length=2,
        max_length=255
    )

    price: float

    stock: int


class ProductUpdate(BaseModel):

    sku: str | None = None

    name: str | None = None

    price: float | None = None

    stock: int | None = None
class ProductResponse(BaseModel):

    id: int

    sku: str

    name: str

    price: float = Field(gt=0)

    stock: int = Field(ge=0)

    class Config:
        from_attributes = True