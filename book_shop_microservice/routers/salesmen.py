from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import SalesmanValidator
from book_shop_microservice.service import salesmen
router_salesman = APIRouter(prefix="/salesman", tags=["SALESMAN"])


@router_salesman.post("/create")
def post_salesman(salesman: SalesmanValidator, session: Session = Depends(get_db)):
    return salesmen.post_salesman(salesman, session)
