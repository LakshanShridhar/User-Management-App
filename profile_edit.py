from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import Base, engine, get_db, User 
from passlib.hash import bcrypt
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


# Intitialize Fast API app
app = FastAPI(lifespan=lifespan)

# Pydantic model for editing the user profile
class UserProfileEdit(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    interests: str

# POST endpoint to handle user profile editing
@app.post("/profile-edit")
def profile_edit(user: UserProfileEdit, db: Session = Depends(get_db)):
    # 1. Fetch user from DB by email
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # 2. Verify password using bcrypt
    if not bcrypt.verify(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    # 3. If password matches, login successful, and update the user's profile information
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.interests = user.interests

    try:
        db.commit()
        db.refresh(db_user) # Gets updated state from DB
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")

    return {"message": "Profile updated successfully"} 