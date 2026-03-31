from fastapi import APIRouter
from app.services.payment_service import PaymentService
from app.models.payment_schema import PaymentRequest

router = APIRouter()

@router.get("/")
def get_status():
    return {"status": "payment service running"}


@router.post("/")
def create_payment(payment: PaymentRequest):
    intent = PaymentService.create_payment(payment.amount)
    return {
        "client_secret": intent.client_secret
    }