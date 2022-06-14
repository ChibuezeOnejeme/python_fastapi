import logging
from pydoc import ModuleScanner
from fastapi import FastAPI, Request,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import Column
from database import session,engine
from sqlalchemy.orm import Session
import models
from schema import whiskey_dantic
from pydantic import validator


models.Base.metadata.create_all(bind=engine)



logging.basicConfig(
    filename='log_file_name.log',
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    filemode='w'
)
app = FastAPI()
templates = Jinja2Templates(directory="templates")



models.Base.metadata.create_all(bind=engine)
logging.info('created database sucessfully')


def get_db():  # for closing the database after opening it
    try:
        db = session
        yield db
    finally:
        db.close()


@app.post("/")  # route defined for api
def create_api(whisk: whiskey_dantic, db: session = Depends(get_db)):

    whisky_model = models.Whiskeys()
   
    whisky_model.name = whisk.name
    whisky_model.price = whisk.price
    db.add(whisky_model)
    db.commit()
    db.close()
    return whisk


@app.get("/")  # route defined for api
def get_api(db: Session = Depends(get_db),):


  
  a =db.query(models.Whiskeys).all()
  return a