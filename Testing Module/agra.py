import requests
from bs4 import BeautifulSoup as bs
import pandas as jd

#url = "https://5bestincity.com/businesses-in-ahmedabad-gj"
url = "https://5bestincity.com/businesses-in-agra-up"
r1 = requests.get(url)

soup1 = bs(r1.text,"html.parser")
cities1 = soup1.find_all("a",class_ = "")

#print(cities)
links1 = []

for link1 in cities1:
    try:
        href1 = link1['href']
    except:
        href1 = None
    if href1:
        if r'businesses' not in href1:
            if r'-in-' in href1:
                
                #print(href)
                jd = "https://5bestincity.com"+href1
                links1.append(jd)
                print(jd)

#print(links1)
print(len(links1))






###### print link of inner page or second page