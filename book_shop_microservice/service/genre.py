from book_shop_microservice.models import Genre
from book_shop_microservice.schemes.sheme import GenreValidator


def post_genre(genre: GenreValidator, db):
    db_genre = Genre(genre_name=genre.genre_name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre