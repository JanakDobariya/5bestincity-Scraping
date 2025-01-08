import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd 

url = "https://5bestincity.com/businesses-in-agra-up"

r = requests.get(url)

soup = bs(r.text,"html.parser")
cat = soup.find_all("div",  attrs={"class" : "col-md-3"})

for i in cat:
    n = i.find_all("h3")
    for nn in range(len(n)):
        print(n[nn].text)
        # print(list(i.find_all("ul"))[mm]) 
        for g in list(i.find_all("ul"))[nn].find_all("h4"):
            u = g.text
            s = g.find("a")["href"]
            u = u.replace("\n","")    
            print("- "+u)
            print("- https://5bestincity.com" +s)
        #for s in list(i.find_all("ul"))[nn].find_all("a"):

    print("\n")







    # for g in list(i.find_all("ul"))[nn]:
        #     for h in g.find_all("h4"):
        #         u = h.text
        #         u = u.replace("\n","")    
        #         print(u)