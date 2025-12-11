# File: backend/app/services/auth_service.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.schemas.user import UserCreate, UserLogin
from backend.app.utils.jwt_handler import create_access_token

class AuthService:
    @staticmethod
    def register_user(db: Session, user_data: UserCreate):
        user = db.query(User).filter(User.email == user_data.email).first()
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )
        new_user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            role=user_data.role,
        )
        new_user.set_password(user_data.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate_user(db: Session, login_data: UserLogin):
        user = db.query(User).filter(User.email == login_data.email).first()
        if not user or not user.verify_password(login_data.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials."
            )
        access_token = create_access_token(data={"sub": user.email, "role": user.role})
        return {"access_token": access_token, "token_type": "bearer"}