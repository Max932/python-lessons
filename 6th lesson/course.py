import requests
from bs4 import BeautifulSoup 
from datetime import datetime

Url = "https://www.cbr.ru/scripts/XML_daily.asp?"

response = requests.get (Url)

soup = BeautifulSoup (response.content, "lxml")

def get_course (id) :
    valute = soup.find ("valute" , {"id" : id})
    return valute.value.text