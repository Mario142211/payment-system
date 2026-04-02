import stripe
import json
import os

from fastapi import APIRouter, Request
from dotenv import load_dotenv

from app.db.database import SessionLocal
from app.models.payment import Payment

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET")

router = APIRouter()


@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()

    event = json.loads(payload.decode("utf-8"))

    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]

        print("Pago exitoso:", payment_intent["id"])

        db = SessionLocal()

        payment = db.query(Payment).order_by(Payment.id.desc()).first()

        if payment:
            payment.status = "paid"
            db.commit()

        db.close()

    return {"status": "ok"}