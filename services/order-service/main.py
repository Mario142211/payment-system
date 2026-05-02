from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.order_controller import router as order_router

app = FastAPI()
origins = [
    "http://localhost:3000",   # frontend local
    "http://127.0.0.1:3000",
    "http://52.14.111.202",
    "http://127.0.0.1:5173",# opcional
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,   # o ["*"] para pruebas
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(order_router, prefix="/orders")