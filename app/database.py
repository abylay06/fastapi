from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
from psycopg.rows import dict_row
from .config import settings

engine = create_engine(f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}', )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# try:
#     conn = psycopg.connect(host="localhost", dbname="fastapi", user="postgres", 
#                             password="0913", port=5432, row_factory=dict_row)
#     cursor = conn.cursor()
#     print("Database connection was successful")
# except Exception as error:
#     print("connection to database failed!")
#     print ("error: ", error)