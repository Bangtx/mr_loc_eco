from schema.base import BaseSchema
from fastapi import UploadFile
from typing import List
from schema.category import Category


class Image(BaseSchema):
    id: int = None
    url: str = None
    payload: str = None


class ProductBase(BaseSchema):
    name: str
    category: int
    cost: int
    price: int
    star: int = 5
    images: List[Image]
    description: str = None
    sales: int = 100
    comment: str = None
    ship_comment: str = None


class Product(ProductBase):
    id: int
    category: Category
    images: List[Image]


class ProductCreate(ProductBase):
    pass
