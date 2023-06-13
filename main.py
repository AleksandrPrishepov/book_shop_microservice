import uvicorn
from fastapi import FastAPI
from book_shop_microservice.routers import authors, books, genre, salesmen, login


app = FastAPI()
app.include_router(authors.router_author)
app.include_router(books.router_book)
app.include_router(genre.router_genre)
app.include_router(salesmen.router_salesman)
app.include_router(login.router_auth)

if __name__ == '__main__':
    uvicorn.run(app)
