from fastapi import FastAPI
from app.controllers.payment_controller import router as payment_router
from app.controllers.webhook_controller import router as webhook_router
from app.db.database import engine, Base

app = FastAPI()

app.include_router(payment_router, prefix="/payments")
app.include_router(webhook_router)

Base.metadata.create_all(bind=engine)