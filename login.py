from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import Base, engine, get_db, User # type: ignore
from passlib.hash import bcrypt
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


# Intitialize Fast API app
app = FastAPI(lifespan=lifespan)

# Pydantic model for verifying login data
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# POST endpoint to handle user login
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # 1. Fetch user from DB by email
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # 2. Verify password using bcrypt
    if not bcrypt.verify(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # 3. If password matches, login successful
    return {"message": f"Welcome back, {db_user.first_name}!"}