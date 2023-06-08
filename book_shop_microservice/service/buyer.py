from book_shop_microservice.models import Buyer
from book_shop_microservice.schemes.sheme import BuyerVaidator


def post_buyer(buyer: BuyerVaidator, db):
    db_buyer = Buyer(buyer_name=buyer.buyer_name, city=buyer.city)
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer