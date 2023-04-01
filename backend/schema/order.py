from schema.base import BaseSchema
from schema.product import Product
from schema.user import User


class Order(BaseSchema):
    id: int
    user: User
    product: Product
    quantity: int
    status: str = None


class OrderCreate(BaseSchema):
    user: int
    product: int
    quantity: int
    status: str = None
