from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import Base, engine, get_db, User
from passlib.hash import bcrypt
from sqlalchemy.exc import IntegrityError
from contextlib import asynccontextmanager

# Define startup event to ensure tables are created
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # Create database tables at startup
    yield

# Initialize FastAPI app with lifespan context
app = FastAPI(lifespan=lifespan)

# Pydantic model for incoming signup data
class UserSignup(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    interests: str

# GET endpoint to provide signup instruction
@app.get("/signup")
def read_signup_info():
    return {"message": "Use POST to submit signup information."}

# POST endpoint to handle user signup
@app.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    try:
        # Hash the password for secure storage
        hashed_password = bcrypt.hash(user.password)

        # Create a new user instance
        new_user = User(
            email=user.email,
            password_hash=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name,
            interests=user.interests
        )
        db.add(new_user)      # Add new user to session
        db.commit()           # Commit transaction
        db.refresh(new_user)  # Refresh to access auto-generated ID

        return {
            "message": "User signed up successfully", 
            "user_id": new_user.id
        }

    except IntegrityError:
        db.rollback()  # Roll back on conflict (e.g. duplicate email)
        raise HTTPException(status_code=400, detail="Email already registered")

# GET endpoint to retrieve user details by ID
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "interests": user.interests
    }