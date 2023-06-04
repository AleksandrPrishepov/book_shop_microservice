import uvicorn
from fastapi import FastAPI
from book_shop_microservice.routers import main_router_api


app = FastAPI()
app.include_router(main_router_api)

# if __name__ == '__main__':
#     uvicorn.run(app)
