from schema.base import BaseSchema
from schema.product import Product
from schema.user import User


class Purchase(BaseSchema):
    id: int
    user: User
    product: Product
    quantity: int
    status: str = None


class PurchaseCreate(BaseSchema):
    user: int
    product: int
    quantity: int
    status: str = None
