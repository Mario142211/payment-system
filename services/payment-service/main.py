from fastapi import FastAPI
from app.controllers.payment_controller import router as payment_router
from app.db.database import engine, Base

app = FastAPI()

app.include_router(payment_router, prefix="/payments")

Base.metadata.create_all(bind=engine)