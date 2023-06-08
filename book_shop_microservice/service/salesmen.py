from book_shop_microservice.models.salesmen import Salesman
from book_shop_microservice.schemes.sheme import SalesmanValidator


def post_salesman(salesman: SalesmanValidator, db):
    db_salesman = Salesman(salesman_name=salesman.salesman_name, age=salesman.age)
    db.add(db_salesman)
    db.commit()
    db.refresh(db_salesman)
    return db_salesman