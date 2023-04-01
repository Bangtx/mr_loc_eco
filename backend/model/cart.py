from peewee import BooleanField, IntegerField, ForeignKeyField, fn, JOIN
from model.base import BaseModel
from model.user import User
from model.product import Product
from model.image import Image


class Cart(BaseModel):
    user = ForeignKeyField(User)
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    is_ordered = BooleanField()
    name = None

    @classmethod
    def get_list(cls, **kwargs):
        products = (
            Product.select(
                Product.id,
                Product.name,
                Product.cost,
                Product.price,
                fn.array_agg(
                    fn.json_build_object(
                        'id', Image.id, 'url', Image.url
                    )
                ).alias('images')
            ).join(
                Image, on=Image.id == fn.any(Product.images)
            ).where(
                Product.active
            ).group_by(
                Product.id
            )
        )

        query = cls.select(
            cls.id,
            fn.json_build_object(
                'id', User.id, 'name', User.name
            ).alias('user'),
            cls.quantity,
            cls.is_ordered,
            fn.json_build_object(
                'id', products.c.id,
                'name', products.c.name,
                'price', products.c.price,
                'cost', products.c.cost,
                'images', products.c.images
            ).alias('product')
        ).join(
            User, on=User.id == cls.user
        ).join(
            products, JOIN.LEFT_OUTER, on=products.c.id == cls.product
        ).where(
            cls.active
        ).dicts()
        return list(query)
