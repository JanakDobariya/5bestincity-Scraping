import requests
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

sp = "https://5bestincity.com/oncologists-in-agra-up"
r = requests.get(sp)

soup2 = bs(r.text, "html.parser")
in5 = soup2.find_all("h3", class_="notranslate")
in6 = soup2.find_all("span", class_="rating-star")

for name,rate in zip(in5,in6):
    name1 = name.text
    name1 = name1.replace("\n","")

    rate1 = rate.text  
    abc = rate1.replace("\n","Hello")
    rate = abc.split("Hello")[1]
    rate3 = abc.split("Hello")[-2]

    print(name1)
    print(rate)
    print(rate3)



# for rate in in6:
#     rate1 = rate.text  
#     abc = rate1.replace("\n","Hello")
#     rate = abc.split("Hello")[1]
#     rate3 = abc.split("Hello")[-2]

#     print(rate)
#     print(rate3)
    