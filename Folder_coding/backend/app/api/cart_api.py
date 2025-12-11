from fastapi import APIRouter
from app.services.cart_service import CartService

cart_router = APIRouter()
cart_service = CartService()

cart_router.post('/cart')
def create_cart(user_id: int):
    cart = cart_service.get_cart(user_id)
    return {'cart_id': cart.user_id}

cart_router.post('/cart/add')
def add_product_to_cart(user_id: int, product_id: int, quantity: int):
    cart = cart_service.get_cart(user_id)
    cart.add_product(product_id, quantity)
    cart_service.save_cart(cart)
    return {'message': 'Product added to cart'}