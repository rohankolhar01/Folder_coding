from fastapi import APIRouter, Depends
from backend.models import Product
from backend.database import get_db

router = APIRouter()