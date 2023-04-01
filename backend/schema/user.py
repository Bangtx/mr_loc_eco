from schema.base import BaseSchema


class UserBase(BaseSchema):
    name: str
    code: int
    tel: str
    email: str = None
    role: int = 0


class User(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass

