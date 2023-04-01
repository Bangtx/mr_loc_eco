from fastapi import APIRouter
from router import category, product, image, user, cart, order

router = APIRouter()


router.include_router(
    category.router,
    prefix='/category',
    tags=['category']
)


router.include_router(
    product.router,
    prefix='/product',
    tags=['product']
)

router.include_router(
    image.router,
    prefix='/image',
    tags=['image']
)

router.include_router(
    user.router,
    prefix='/user',
    tags=['user']
)

router.include_router(
    cart.router,
    prefix='/cart',
    tags=['cart']
)

router.include_router(
    order.router,
    prefix='/order',
    tags=['order']
)


