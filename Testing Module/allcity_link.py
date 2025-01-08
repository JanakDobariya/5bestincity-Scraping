import requests
from bs4 import BeautifulSoup as bs
import pandas as jd

url = "https://5bestincity.com/"
r = requests.get(url)

soup = bs(r.text,"html.parser")
cities = soup.find_all("div",attrs={"class":"col-lg-2 col-md-6"})
links = []

for link in cities:
    
    try:
        href = link.find("a")['href']
    except:
        href = None
    if href:
        if r'https://5bestincity.com/businesses-in' in href:
            if href not in links:
                links.append(href)
                print(href)
    
# print("\n")
#print(links)
print(len(links))


#### print all the city link from home page







# https://5bestincity.com/oncologists-in-agra-up