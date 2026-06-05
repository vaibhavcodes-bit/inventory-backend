# Product routes for CRUD operations
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.product import Product

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)



@router.post(
    "/",
    response_model=ProductResponse
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    existing_product = db.query(Product)\
        .filter(
            Product.sku == product.sku
        )\
        .first()

    if existing_product:

        raise HTTPException(
            status_code=400,
            detail="SKU already exists"
        )

    db_product = Product(
        **product.model_dump()
    )

    db.add(db_product)

    db.commit()

    db.refresh(db_product)

    return db_product


@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):

    offset = (page - 1) * limit

    products = db.query(Product)\
        .offset(offset)\
        .limit(limit)\
        .all()

    return products


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product)\
        .filter(
            Product.id == product_id
        )\
        .first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product



@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):

    product = db.query(Product)\
        .filter(
            Product.id == product_id
        )\
        .first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    update_data = product_data.model_dump(
        exclude_unset=True
    )

    # Check duplicate SKU if SKU is being updated
    if "sku" in update_data:

        existing = db.query(Product)\
            .filter(
                Product.sku == update_data["sku"],
                Product.id != product_id
            )\
            .first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="SKU already exists"
            )

    # Update only provided fields
    for key, value in update_data.items():

        setattr(
            product,
            key,
            value
        )

    db.commit()

    db.refresh(product)

    return product

@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product)\
        .filter(
            Product.id == product_id
        )\
        .first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)

    db.commit()

    return {
        "message":
        "Product deleted successfully"
    }