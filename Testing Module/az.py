import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

url5 = 'https://5bestincity.com/'
r5 = requests.get(url5)

soup5 = bs(r5.text,"html.parser")
cities5 = soup5.find_all("div",class_ = "col-lg-2 col-md-6")

name15 = []
for city5 in cities5:
    name5 = city5.text
    name5 = name5.replace('\n','')
    name15.append(name5)
    
#####
r7 = requests.get(url5)

soup7 = bs(r7.text,"html.parser")
cities7 = soup7.find_all("div",attrs={"class":"col-lg-2 col-md-6"})
links7 = []

for link7 in cities7:
    
    try:
        href7 = link7.find("a")['href']
    except:
        href7 = None
    if href7:
        if r'https://5bestincity.com/businesses-in' in href7:
            if href7 not in links7:
                links7.append(href7)


for item1, item2 in zip(name15, links7):
    print(item1, item2)