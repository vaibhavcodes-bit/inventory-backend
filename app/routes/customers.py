# Customer routes for CRUD operations
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post(
    "/",
    response_model=CustomerResponse
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Customer)\
        .filter(
            Customer.email == customer.email
        )\
        .first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    db_customer = Customer(
        **customer.model_dump()
    )

    db.add(db_customer)

    db.commit()

    db.refresh(db_customer)

    return db_customer


@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer)\
        .filter(
            Customer.id == customer_id
        )\
        .first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer)\
        .filter(
            Customer.id == customer_id
        )\
        .first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    update_data = customer_data.model_dump(
        exclude_unset=True
    )

    # Check duplicate email if email is being updated
    if "email" in update_data:

        existing = db.query(Customer)\
            .filter(
                Customer.email == update_data["email"],
                Customer.id != customer_id
            )\
            .first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    # Update only provided fields
    for key, value in update_data.items():

        setattr(
            customer,
            key,
            value
        )

    db.commit()

    db.refresh(customer)

    return customer


@router.delete(
    "/{customer_id}"
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = db.query(Customer)\
        .filter(
            Customer.id == customer_id
        )\
        .first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)

    db.commit()

    return {
        "message":
        "Customer deleted successfully"
    }