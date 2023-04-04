from fastapi import APIRouter
from model.cart import Cart as CartModel
from schema.cart import Cart, CartCreate
from typing import List
from ultils.db import transaction

router = APIRouter()


@router.get('/')
def get_cart(user: int = None):
    return CartModel.get_list(user=user)


@router.post('/')
@transaction
def create_cart(cart: CartCreate):
    return CartModel.create(**cart.dict())


@router.delete('/{id}')
@transaction
def delete_cart(id: int):
    return CartModel.soft_delete(id)
