


from pyexpat import model
from random import Random
from sqlite3 import Time
from tokenize import Name
from bs4 import BeautifulSoup
import requests
import time
import numpy
import pandas as pd
import csv
from database import session, engine
import models
from schema import whiskey_dantic

#from sqlalchemy.orm import Session
from sqlalchemy import insert



def get_info():

   website = 'https://www.jumia.com.ng/whiskey/'

   html_text = requests.get(website).text
   soup = BeautifulSoup(html_text, 'lxml')
   whiskeys = soup.find_all('div', class_='info')

   with open('data.csv', 'w', newline='', encoding="utf-8") as f:
       the_writer = csv.writer(f,)
       header = ['name', 'price']
       the_writer.writerow(header)
       for whiskey in whiskeys:
           whiskey_name = whiskey.find('h3', class_='name').text
           whiskey_price = whiskey.find('div', class_='prc').text
           #saving to csv file
           whisk_data1 = [whiskey_name, whiskey_price]
           the_writer.writerow(whisk_data1)
           # saving to database sqlite
           #whiskey_data =models.Whiskeys(name=whiskey_name,price=whiskey_price)


def cv_sql():
   with open('data.csv', 'rb') as file:
       data_df = pd.read_csv(file)
       
      
       a = data_df.to_sql('books', con=engine, index=False,
                          if_exists='append' )



      



def intialize_B4_save_cs4_to_sql():

    get_info()
    
    cv_sql()
if __name__ == '__main__':
    while True:
        intialize_B4_save_cs4_to_sql()
        time_wait = 20
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 1)



















    
  

    