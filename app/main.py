from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order

from app.routes.products import router as product_router
from app.routes.customers import router as customer_router
from app.routes.orders import router as order_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management API"
)

app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)


@app.get("/")
def root():
    return {
        "message": "Inventory API Running"
    }