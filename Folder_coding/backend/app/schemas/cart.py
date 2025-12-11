from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: int
    quantity: int

class Cart(BaseModel):
    user_id: int
    products: List[CartItem]