from fastapi import FastAPI
from .api import cart

app = FastAPI(title='Shopping Cart Service', version='1.0.0')

app.include_router(cart.router)

@app.get('/')
def root():
    return {'message': 'Shopping Cart API running'}