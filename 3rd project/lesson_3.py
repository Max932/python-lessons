import requests
from bs4 import BeautifulSoup 

def temp (html) : 
    return html.find ("span" , {"class" : "temp__value"}).text
def condition (html) :
    return html.find ("div" , {"class" : "day-anchor"}).text

url = "https://yandex.ru/pogoda/yakutsk?from=serp_title"
response = requests.get (url)
html = BeautifulSoup (response.content, "lxml")
print (temp(html))
print (condition(html))

hours = 3

sunset = 18
sunrise = 6

if hours > sunrise and hours < sunset :
    print ("на улице солнце")




















