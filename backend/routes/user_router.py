from fastapi import APIRouter, Depends
from backend.models import User
from backend.database import get_db

router = APIRouter()