'''FastAPI router for managing products.'''

from __future__ import annotations
import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate

logger = logging.getLogger(__name__)
router = APIRouter(prefix='/products', tags=['Products'])

@router.post('/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)) -> ProductResponse:
    '''Create a new product.'''
    existing = db.query(Product).filter(Product.name == product.name).first()
    if existing:
        logger.warning('Product with name %s already exists', product.name)
        raise HTTPException(status_code=400, detail='Product already exists')

    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get('/', response_model=List[ProductResponse])
def list_products(db: Session = Depends(get_db)) -> List[ProductResponse]:
    '''Retrieve all products.'''
    return db.query(Product).all()

@router.get('/{product_id}', response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    '''Retrieve a product by ID.'''
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        logger.error('Product %s not found', product_id)
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.put('/{product_id}', response_model=ProductResponse)
def update_product(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)) -> ProductResponse:
    '''Update a product by ID.'''
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        logger.error('Product %s not found for update', product_id)
        raise HTTPException(status_code=404, detail='Product not found')

    for key, value in product_update.dict(exclude_unset=True).items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product

@router.delete('/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)) -> None:
    '''Delete a product.'''
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        logger.warning('Product %s not found for deletion', product_id)
        raise HTTPException(status_code=404, detail='Product not found')

    db.delete(product)
    db.commit()
    logger.info('Product %s deleted successfully', product_id)
    return None