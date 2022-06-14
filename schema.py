
from distutils.command.config import config
from pandas import notnull
from pydantic import BaseModel, Field
from typing import List

from sqlalchemy import true


class whiskey_dantic(BaseModel):
    name: str = Field(min_length=1)
    price:str= Field(min_length=1, max_length=100)
    class Config:
        orm_mode =True


        


