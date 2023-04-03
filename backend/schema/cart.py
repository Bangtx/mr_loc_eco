from schema.purchase import Purchase, PurchaseCreate


class Cart(Purchase):
    pass


class CartCreate(PurchaseCreate):
    status: str = 'not_order'




