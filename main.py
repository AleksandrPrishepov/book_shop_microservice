import uvicorn
from fastapi import FastAPI
from book_shop_microservice.routers import authors, books, buyer, genre, salesmen


app = FastAPI()
app.include_router(authors.router_author)
app.include_router(books.router_book)
app.include_router(buyer.router_buyer)
app.include_router(genre.router_genre)
app.include_router(salesmen.router_salesman)

# if __name__ == '__main__':
#     uvicorn.run(app)
