from schema.base import BaseSchema
from schema.product import Product
from schema.user import User


class Cart(BaseSchema):
    id: int
    user: User
    product: Product
    quantity: int
    is_ordered: bool = False


class CartCreate(BaseSchema):
    user: int
    product: int
    quantity: int
    is_ordered: bool = False





