from fastapi import APIRouter
from model.cart import Cart as CartModel
from schema.cart import Cart, CartCreate
from typing import List

router = APIRouter()


@router.get('/')
def get_cart(user: int):
    return CartModel.get_list(get_dict=False, user=user)


@router.post('/', response_model=Cart)
def create_cart(cart: CartCreate):
    return CartModel.create(**cart.dict())
