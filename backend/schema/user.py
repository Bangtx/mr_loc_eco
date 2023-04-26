from schema.base import BaseSchema


class UserBase(BaseSchema):
    name: str
    code: str
    tel: str
    email: str
    role: int = 0
    address: str = None


class User(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class UserLogin(BaseSchema):
    code: str
    password: str

