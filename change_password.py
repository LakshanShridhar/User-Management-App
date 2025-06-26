from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from database import get_db, User

app = FastAPI()

class PasswordChangeRequest(BaseModel):
    email: EmailStr
    current_password: str
    new_password: str

@app.post("/change-password")
def change_password(data: PasswordChangeRequest, db: Session = Depends(get_db)):
    # Retrieve user by email
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        # User not found in database
        raise HTTPException(status_code=404, detail="User not found")

    # Check if current password matches stored hash
    if not bcrypt.verify(data.current_password, user.password_hash):
        # Current password is incorrect
        raise HTTPException(status_code=400, detail="Incorrect current password")

    # Hash new password and update user record
    user.password_hash = bcrypt.hash(data.new_password)
    db.commit()       # Commit changes to DB
    db.refresh(user)  # Refresh user instance

    return {"message": "Password updated successfully"}