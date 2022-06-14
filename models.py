from email.policy import default
from pickle import TRUE
from pandas import unique
from sqlalchemy import Column, Integer, String,DateTime, UniqueConstraint, null
from database import Base
from datetime import datetime

class Whiskeys(Base):

    __tablename__ = "books"
  
    id = Column(Integer, primary_key=True, index=True,unique=True)
    name = Column(String)
    price = Column(String)