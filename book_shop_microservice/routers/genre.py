from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from book_shop_microservice.core.database import get_db
from book_shop_microservice.schemes.sheme import GenreValidator
from book_shop_microservice.service import genre

router_genre = APIRouter(prefix="/genre", tags=["GENRE"])


@router_genre.post("/create")
def post_genre(genr: GenreValidator, session: Session = Depends(get_db)):
    return genre.post_genre(genr, session)
