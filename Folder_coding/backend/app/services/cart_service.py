from app.core.cart import Cart
from app.schemas.cart import Cart as CartSchema

class CartService:
    def __init__(self):
        self.carts = {}

    def get_cart(self, user_id: int):
        if user_id not in self.carts:
            self.carts[user_id] = Cart(user_id)
        return self.carts[user_id]

    def save_cart(self, cart: Cart):
        self.carts[cart.user_id] = cart