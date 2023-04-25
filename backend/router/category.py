from fastapi import APIRouter
from model.category import Category
from schema import category as schema
from typing import List
from model.image import Image
from base64 import b64decode
from ultils.db import transaction


router = APIRouter()


@router.get('/')
def get_categories():
    return Category.get_list()


@router.post('/')
@transaction
def create_category(category: schema.CategoryCreate):
    category = category.dict()
    if category['logo']['payload']:
        img = Image.create(b64decode(category['logo']['payload'].split(',').pop()))
        category['image'] = img.id
    category.pop('logo', None)
    return Category.create(**category)


@router.put('/{id}')
@transaction
def update_category(id: int, category: schema.CategoryCreate):
    category = category.dict()
    if category['logo']['payload']:
        img = Image.create(b64decode(category['logo']['payload'].split(',').pop()))
        category['image'] = img.id
    category.pop('logo', None)
    return Category.update(**category).where(Category.id == id).execute()
