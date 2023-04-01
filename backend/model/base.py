from peewee import CharField, Model, BooleanField
from operator import attrgetter
from config.database import db


class BaseModel(Model):
    name = CharField()
    active = BooleanField()

    class Meta:
        database = db

    @classmethod
    def get_list(cls, get_dict=True, **kwargs):
        query = cls.handle_select()

        for key, value in kwargs.items():
            query = query.where(attrgetter(key)(cls) == value)

        if get_dict:
            query = query.dicts()

        query = query.order_by(cls.id)
        return list(query)

    @classmethod
    def handle_select(cls):
        return cls.select().where(cls.active)
