'''Product model definition for the product catalog.'''

from __future__ import annotations
import logging
from typing import Optional
from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

logger = logging.getLogger(__name__)
Base = declarative_base()

class Product(Base):
    '''SQLAlchemy model representing a product in the catalog.'''

    __tablename__ = 'products'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False, unique=True)
    description: Optional[str] = Column(Text, nullable=True)
    price: float = Column(Float, nullable=False)
    category_id: int = Column(Integer, ForeignKey('categories.id'))

    category = relationship('Category', back_populates='products')

    def __repr__(self) -> str:
        return f'<Product(name={self.name}, price={self.price})>'

class Category(Base):
    '''SQLAlchemy model representing product categories.'''

    __tablename__ = 'categories'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(255), nullable=False, unique=True)

    products = relationship('Product', back_populates='category', cascade='all, delete')