import requests
from bs4 import BeautifulSoup
import pandas as pd

url3 = "https://5bestincity.com/businesses-in-agra-up"
r = requests.get(url3)

soup3 = BeautifulSoup(r.text, "html.parser")
#cities = soup.find_all("a",class_ = "list")
cities3 = soup3.find_all("h4")

name_list3 = []

for city3 in cities3: 
#    try:
        #print(city.find("h4").find("a").text)
        name3 = city3.find("a").text
        #print(name)
        name3 = name3.replace('\n', '')
        name_list3.append(name3)
#    except:
#        pass

print(name_list3)
#print(len(name_list3))

# for i in name_list:
#     print(i)
