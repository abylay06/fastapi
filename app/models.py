from .database import Base
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Deposit(Base):
    __tablename__ = "deposits"
    id = Column(Integer, primary_key=True, nullable=False)
    purpose = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Report(Base):
    __tablename__ = "reports"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    deposit_id = Column(Integer, ForeignKey("deposits.id", ondelete="CASCADE"), primary_key=True)