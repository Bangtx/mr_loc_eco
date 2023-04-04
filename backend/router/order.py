from fastapi import APIRouter
from model.order import Order as OrderModel
from schema.order import Order, OrderCreate
from typing import List
from ultils.db import transaction

router = APIRouter()


@router.get('/')
def get_order(user: int):
    return OrderModel.get_list(user=user)


@router.post('/', response_model=Order)
@transaction
def create_order(cart: OrderCreate):
    return OrderModel.create(**cart.dict())


@router.delete('/{id}')
@transaction
def delete_order(id: int):
    return OrderModel.soft_delete(id)
