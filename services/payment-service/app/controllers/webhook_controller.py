import stripe
import os

from fastapi import APIRouter, Request, HTTPException
from dotenv import load_dotenv

from app.db.database import SessionLocal
from app.models.payment import Payment

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

router = APIRouter()


@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]

        db = SessionLocal()

        payment = db.query(Payment) \
            .filter(Payment.stripe_id == payment_intent["id"]) \
            .first()

        if payment:
            payment.status = "paid"
            db.commit()

        db.close()

    return {"status": "ok"}