from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

class Cart(BaseModel):
    user_id: int
    products: list[Product]