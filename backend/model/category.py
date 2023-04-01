from model.base import BaseModel
from peewee import IntegerField, ForeignKeyField, fn
from model.image import Image


class Category(BaseModel):
    parent = IntegerField()
    image = ForeignKeyField(Image, column_name='image')

    class Meta:
        db_table = 'category'

    @classmethod
    def handle_select(cls):
        return (
            cls.select(
                cls.id, cls.name,
                fn.json_build_object(
                    'id', Image.id, 'url', Image.url
                ).alias('logo')
            ).left_outer_join(
                Image, on=Image.id == cls.image
            )
        )

