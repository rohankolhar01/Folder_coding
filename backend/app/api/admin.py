from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class AdminDashboard(BaseModel):
    sales: int
    inventory: int
    user_activity: int

@app.get('/admin/')
def get_admin_dashboard():
    return {'sales': 100, 'inventory': 50, 'user_activity': 200}