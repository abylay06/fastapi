from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class BaseDeposit(BaseModel):
    purpose: str
    amount: int
    receiver: str = "John"

class CreateDeposit(BaseDeposit):
    pass

class OutUser(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Deposit(BaseDeposit):
    created_at: datetime
    id: int
    owner_id: int
    owner: OutUser
    
    class Config:
        orm_mode = True



class User(BaseModel):
    email: EmailStr
    password: str



class Login(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Report(BaseModel):
    deposit_id: int
    dir: conint(le=1)

class DepositWithReports(BaseModel):
    Deposit: Deposit
    reports: int
    class Config:
        from_attributes = True