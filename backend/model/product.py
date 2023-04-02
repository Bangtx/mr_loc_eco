from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField, fn, SQL
from model.category import Category
from model.image import Image
from playhouse.postgres_ext import ArrayField
from playhouse.shortcuts import model_to_dict
from operator import attrgetter


class Product(BaseModel):
    category = ForeignKeyField(Category, column_name='category')
    cost = IntegerField()
    price = IntegerField()
    star = IntegerField()
    images = ArrayField()
    description = CharField()
    sales = IntegerField()
    comment = CharField()
    ship_comment = CharField()

    class Meta:
        db_table = 'product'

    @classmethod
    def get_list(cls, limit=None, **kwargs):
        query = (
            cls.select(
                cls.id,
                cls.name,
                cls.price,
                cls.cost,
                cls.comment,
                cls.ship_comment,
                cls.sales,
                cls.star,
                cls.description,
                fn.json_build_object(
                    'id', Category.id, 'name', Category.name
                ).alias('category'),
                fn.array_agg(
                    fn.json_build_object(
                        'id', Image.id, 'url', Image.url, 'path', Image.path
                    )
                ).alias('images')
            ).join(
                Category, on=Category.id == cls.category
            ).left_outer_join(
                Image, on=Image.id == fn.any(cls.images)
            ).group_by(
                cls.id, Category.id
            ).dicts()
        )

        for key, value in kwargs.items():
            if value:
                query = query.where(attrgetter(key)(cls) == value)

        if limit:
            query = query.limit(limit)

        return list(query)
