from peewee import CharField, IntegerField
from model.base import BaseModel


class User(BaseModel):
    code = IntegerField()
    tel = CharField()
    email = CharField()
    address = CharField()
    role = IntegerField()

