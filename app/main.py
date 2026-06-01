from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.product import Product
from app.models.customer import Customer
from app.models.order import Order

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Inventory Management API"
)

@app.get("/")
def root():
    return {
        "message": "Inventory API Running"
    }