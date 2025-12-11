from typing import List

class Cart:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.products = []

    def add_product(self, product_id: int, quantity: int):
        self.products.append({'product_id': product_id, 'quantity': quantity})

    def remove_product(self, product_id: int):
        self.products = [product for product in self.products if product['product_id'] != product_id]

    def modify_product(self, product_id: int, quantity: int):
        for product in self.products:
            if product['product_id'] == product_id:
                product['quantity'] = quantity
                break