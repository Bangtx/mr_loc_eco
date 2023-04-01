from fastapi import APIRouter
from model.order import Order as OrderModel
from schema.order import Order, OrderCreate
from typing import List

router = APIRouter()


@router.get('/')
def get_order(user: int):
    return OrderModel.get_list(get_dict=False, user=user)


@router.post('/', response_model=Order)
def create_order(cart: OrderCreate):
    return OrderModel.create(**cart.dict())
