from schema.base import BaseSchema


class Logo(BaseSchema):
    payload: str = None


class Category(BaseSchema):
    id: int
    name: str
    parent: int = None
    logo: str = None


class CategoryCreate(BaseSchema):
    name: str
    parent: int = None
    logo: Logo


class CategoryUpdate(BaseSchema):
    name: str
    parent: int = None
    logo: Logo