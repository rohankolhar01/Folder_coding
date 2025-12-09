from fastapi import APIRouter, Depends

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login():
    return {"message": "Login endpoint"}

@router.post("/signup")
def signup():
    return {"message": "Signup endpoint"}