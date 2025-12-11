from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from ... import models

router = APIRouter(prefix='/cart', tags=['Cart'])

@router.post('/add/{product_id}')
def add_to_cart(product_id: int, quantity: int = 1, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')

    cart = db.query(models.Cart).filter(models.Cart.user_id == None).first()
    if not cart:
        cart = models.Cart(user_id=None)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    cart_item = db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id, models.CartItem.product_id == product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = models.CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.add(cart_item)

    db.commit()
    db.refresh(cart_item)
    return {'message': 'Item added to cart', 'cart_item_id': cart_item.id}

@router.delete('/remove/{product_id}')
def remove_from_cart(product_id: int, db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == None).first()
    if not cart:
        raise HTTPException(status_code=404, detail='Cart not found')

    item = db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id, models.CartItem.product_id == product_id).first()
    if not item:
        raise HTTPException(status_code=404, detail='Item not in cart')

    db.delete(item)
    db.commit()
    return {'message': 'Item removed from cart'}

@router.get('/')
def view_cart(db: Session = Depends(get_db)):
    cart = db.query(models.Cart).filter(models.Cart.user_id == None).first()
    if not cart:
        return {'items': []}

    items = db.query(models.CartItem).filter(models.CartItem.cart_id == cart.id).all()
    result = []
    for item in items:
        product = db.query(models.Product).filter(models.Product.id == item.product_id).first()
        result.append({
            'product_id': item.product_id,
            'product_name': product.name,
            'quantity': item.quantity,
            'price_per_unit': product.price,
            'total_price': product.price * item.quantity
        })
    return {'items': result}