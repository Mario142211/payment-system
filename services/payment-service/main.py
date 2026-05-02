from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 IMPORTAR MODELOS PRIMERO (CLAVE)
from app.models.payment import Payment

# luego todo lo demás
from app.controllers.payment_controller import router as payment_router
from app.controllers.webhook_controller import router as webhook_router
from app.controllers.auth_controller import router as auth_router
from app.db.database import engine, Base

app = FastAPI()
origins = [
    "http://localhost:3000",   # frontend local
    "http://127.0.0.1:3000",
    "http://52.14.111.202",
    "http://127.0.0.1:5173",# opcional
    "http://localhost:5173",# opcional
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,   # o ["*"] para pruebas
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(payment_router, prefix="/payments")
app.include_router(webhook_router)
app.include_router(auth_router,prefix="/auth")

# 🔥 CREAR TABLAS AL FINAL
Base.metadata.create_all(bind=engine)
