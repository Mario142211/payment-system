import stripe
import os
from dotenv import load_dotenv
from app.db.database import SessionLocal
from app.models.payment import Payment

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET")




class PaymentService:

    @staticmethod
    def create_payment(amount: float):
        intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),
            currency="mxn",
        )

        db = SessionLocal()

        payment = Payment(
            amount=amount,
            status="created"
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        db.close()

        return intent