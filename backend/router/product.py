import os
from fastapi import APIRouter, UploadFile, HTTPException
from model.product import Product
from model.image import Image
from schema import product as schema
from typing import List
import base64
from playhouse.shortcuts import model_to_dict


router = APIRouter()


@router.get('/')
def get_product(category: int = None, limit: int = None):
    return Product.get_list(limit=limit, category=category)


@router.get('/get_one/{id}')
def get_one(id: int):
    product = Product.get_list(id=id)
    if not product:
        HTTPException(400, 'not found product')
    return product[0]


@router.post('/')
def create_product(product: schema.ProductCreate):
    product = product.dict()
    if product['images']:
        images = []
        for i_index, img in enumerate(product['images']):
            new_img = Image.create(base64.b64decode(img['payload'].split(',').pop()), i_index)
            images.append(new_img.id)
        product['images'] = images
    return Product.create(**product)


@router.put('/{id}')
def update_product(id: int, product: schema.ProductCreate):
    product = product.dict()
    if product['images']:
        images = []
        for i_index, img in enumerate(product['images']):
            if img['id']:
                images.append(img['id'])
            else:
                new_img = Image.create(base64.b64decode(img['payload'].split(',').pop()), i_index)
                images.append(new_img.id)
        product['images'] = images
    return Product.update(**product).where(Product.id == id).execute()


@router.delete('/{id}')
def delete_product(id: int):
    # delete product and image
    product = model_to_dict(Product.get_by_id(id))
    images = product['image']

    Product.delete().where(Product.id == product['id']).execute()
    for img in images:
        path = model_to_dict(Image.get_by_id(img))
        path = path['url'].split('/')[-1]
        os.remove(f'image/{path}')
        Image.delete().where(Image.id == img).execute()

    return {'msg': 'deleted ok'}
