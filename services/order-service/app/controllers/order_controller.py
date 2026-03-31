# app/controllers/order_controller.py
from fastapi import APIRouter
from app.services.order_service import OrderService

router = APIRouter()

@router.post("/")
def create_order(amount: float):
    return OrderService.create_order(amount)