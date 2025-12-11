'''Pydantic schemas for product and category data validation.'''

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    '''Base schema for category.'''
    name: str = Field(..., example='Electronics')

class CategoryCreate(CategoryBase):
    '''Schema for creating a category.'''
    pass

class CategoryResponse(CategoryBase):
    '''Schema for returning category data.'''
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    '''Base schema for product.'''
    name: str = Field(..., example='Smartphone')
    description: Optional[str] = Field(None, example='High-performance phone')
    price: float = Field(..., ge=0)
    category_id: int

class ProductCreate(ProductBase):
    '''Schema for creating product.'''
    pass

class ProductUpdate(BaseModel):
    '''Schema for updating product.'''
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    category_id: Optional[int]

class ProductResponse(ProductBase):
    '''Schema for returning product data.'''
    id: int

    class Config:
        orm_mode = True