from fastapi import FastAPI

# 🔥 IMPORTAR MODELOS PRIMERO (CLAVE)
from app.models.payment import Payment

# luego todo lo demás
from app.controllers.payment_controller import router as payment_router
from app.controllers.webhook_controller import router as webhook_router
from app.controllers.auth_controller import router as auth_router
from app.db.database import engine, Base

app = FastAPI()

app.include_router(payment_router, prefix="/payments")
app.include_router(webhook_router)
app.include_router(auth_router,prefix="/auth")

# 🔥 CREAR TABLAS AL FINAL
Base.metadata.create_all(bind=engine)
