# File: backend/app/utils/jwt_handler.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from backend.app.core.config import settings

def create_access_token(data: dict, expires_delta: int = None):
    """Creates a JWT access token with expiry."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(
        minutes=expires_delta or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """Verifies and decodes JWT."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None