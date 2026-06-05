# Customer schemas for request and response validation

from pydantic import BaseModel
from pydantic import EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    address: str


class CustomerUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    address: str | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str
    address: str

    class Config:
        from_attributes = True