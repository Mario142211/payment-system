

from fastapi import APIRouter,HTTPException

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.db.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin

router=APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db=SessionLocal()

    existing=db.query(User).filter(User.email==user.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="el usuario ya existe")

    new_user=User(
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "usuario creado correctamente"}

@router.post("/login")
def login(user: UserLogin):
    db=SessionLocal()

    db_user=db.query(User).filter(User.email==user.email).first()

    if not db_user or not verify_password(user.password,db_user.password):
        raise HTTPException(status_code=401,detail="credeciales incorrectas")

    token= create_access_token({"sub":db_user.email})

    return {"access Token":token}



