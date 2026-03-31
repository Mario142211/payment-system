from fastapi import FastAPI
from app.controllers.order_controller import router as order_router

app = FastAPI()

app.include_router(order_router, prefix="/orders")