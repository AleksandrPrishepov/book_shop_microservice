from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from config import DB_PASS, DB_HOST, DB_NAME, DB_USER
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
