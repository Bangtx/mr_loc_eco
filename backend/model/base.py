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
            if value:
                query = query.where(attrgetter(key)(cls) == value)

        query = query.where(cls.active)
        if get_dict:
            query = query.dicts()

        query = query.order_by(cls.id)
        return list(query)

    @classmethod
    def handle_select(cls):
        return cls.select().where(cls.active)

    @classmethod
    def soft_delete(cls, id):
        return cls.update(active=False).where(cls.id == id).execute()

