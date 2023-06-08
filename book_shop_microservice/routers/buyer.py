from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import BuyerVaidator
from book_shop_microservice.service import buyer


router_buyer = APIRouter(prefix="/buyer", tags=["BUYER"])

@router_buyer.post("/create")
def post_buyer(buye: BuyerVaidator, session: Session = Depends(get_db)):
    return buyer.post_buyer(buye, session)
