from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .routes import deposits, users, auth, reports
from fastapi.middleware.cors import CORSMiddleware

# venv\Scripts\activate
# uvicorn app.main:app --reload

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(deposits.router)
app.include_router(auth.router)
app.include_router(reports.router)

@app.get("/")
def greet():
    return "hello world"







    



        
