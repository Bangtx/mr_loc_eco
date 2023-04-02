from peewee import CharField, IntegerField
from model.base import BaseModel


class User(BaseModel):
    code = CharField()
    tel = CharField()
    email = CharField()
    address = CharField()
    role = IntegerField()
    password = CharField()

