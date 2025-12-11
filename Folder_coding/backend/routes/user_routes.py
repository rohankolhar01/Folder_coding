from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .models import User
from .database import SessionLocal
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Query

app = FastAPI()

class UserRequest(BaseModel):
    username: str
    email: str
    hashed_password: str

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user
@app.post("/users/")
async def create_user(user: UserRequest, db: SessionLocal = get_db()):
    # Check if user already exists
    existing_user = db.query(User).filter(User.username == user.username or User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    # Create new user
    new_user = User(username=user.username, email=user.email, hashed_password=user.hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get all users
@app.get("/users/", response_model=List[User])
async def read_users(db: SessionLocal = get_db()):
    users = db.query(User).all()
    return users

# Get a user by username
@app.get("/users/{username}", response_model=User)
async def read_user(username: str, db: SessionLocal = get_db()):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a user
@app.put("/users/{username}")
async def update_user(username: str, user: UserRequest, db: SessionLocal = get_db()):
    existing_user = db.query(User).filter(User.username == username).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    # Update user
    existing_user.username = user.username
    existing_user.email = user.email
    existing_user.hashed_password = user.hashed_password
    db.commit()
    db.refresh(existing_user)
    return existing_user

# Delete a user
@app.delete("/users/{username}")
async def delete_user(username: str, db: SessionLocal = get_db()):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return JSONResponse(content={"message": "User deleted"}, status_code=200)
