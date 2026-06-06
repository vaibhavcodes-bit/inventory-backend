# Order routes for creating and retrieving orders
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.order import Order
from app.models.product import Product
from app.models.customer import Customer

from app.schemas.order import (
    OrderCreate,
    OrderUpdate,
    OrderResponse
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "/",
    response_model=OrderResponse
)
def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db)
):

    if order.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than 0"
        )

    customer = db.query(Customer)\
        .filter(Customer.id == order.customer_id)\
        .first()

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    product = db.query(Product)\
        .filter(Product.id == order.product_id)\
        .first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product.stock < order.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    total_amount = product.price * order.quantity

    try:

        product.stock -= order.quantity

        db_order = Order(
            customer_id=order.customer_id,
            product_id=order.product_id,
            quantity=order.quantity,
            total_amount=total_amount
        )

        db.add(db_order)

        db.commit()

        db.refresh(db_order)

        db.refresh(product)

        return db_order
    
    except Exception as e:

            db.rollback()

            raise HTTPException(
                status_code=500,
                detail=str(e)
            )



@router.get(
    "/",
    response_model=list[OrderResponse]
)
def get_orders(
    db: Session = Depends(get_db)
):

    return db.query(Order).all()

@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order)\
        .filter(Order.id == order_id)\
        .first()

    if not order:

        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order

@router.put(
    "/{order_id}",
    response_model=OrderResponse
)
def update_order(
    order_id: int,
    order_data: OrderUpdate,
    db: Session = Depends(get_db)
):

    order = db.query(Order)\
        .filter(Order.id == order_id)\
        .first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    product = db.query(Product)\
        .filter(Product.id == order.product_id)\
        .first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = order_data.model_dump(
        exclude_unset=True
    )

    try:

        # Return previous quantity to stock
        product.stock += order.quantity

        new_quantity = update_data.get(
            "quantity",
            order.quantity
        )

        if new_quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than 0"
            )

        if product.stock < new_quantity:
            raise HTTPException(
                status_code=400,
                detail="Insufficient stock"
            )

        # Deduct new quantity
        product.stock -= new_quantity

        if "customer_id" in update_data:

            customer = db.query(Customer)\
                .filter(
                    Customer.id ==
                    update_data["customer_id"]
                )\
                .first()

            if not customer:
                raise HTTPException(
                    status_code=404,
                    detail="Customer not found"
                )

            order.customer_id = update_data["customer_id"]

        order.quantity = new_quantity

        order.total_amount = (
            product.price *
            new_quantity
        )

        db.commit()

        db.refresh(order)

        return order

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )



@router.delete("/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = db.query(Order)\
        .filter(Order.id == order_id)\
        .first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    db.delete(order)

    db.commit()

    return {
        "message": "Order deleted successfully"
    }
    
    
    
    
    
    
    