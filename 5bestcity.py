import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

url = "https://5bestincity.com/"

review_list = []
rate_list = []
businessman_list = []
business_list = []
category_list = []
city_name = []
name15 = []
links = []
links1 = []

r5 = requests.get(url)
soup5 = bs(r5.text,"html.parser")
cities5 = soup5.find_all("div",class_ = "col-lg-2 col-md-6")

for city5 in cities5:
    name5 = city5.text.replace('\n','')
    name15.append(name5)
    # print(name5)

    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    cities = soup.find_all("div", attrs={"class": "col-lg-2 col-md-6"})


    #for link,nam in zip(cities[-1:],name15[-1:]):
    for link,nam in zip(cities,name15):
        try:
            href = link.find("a")["href"]
        except:
            href = None
        if href:
            if r"https://5bestincity.com/businesses-in" in href:
                if href not in links:
                    links.append(href)

                    r1 = requests.get(href)
####
                    soup1 = bs(r1.text,"html.parser")
                    cat = soup1.find_all("div",  attrs={"class" : "col-md-3"})

                    for i in cat:
                        n = i.find_all("h3")
                        for nn in range(len(n)):
                            #print(n[nn].text)
                            # print(list(i.find_all("ul"))[mm]) 
                            for g in list(i.find_all("ul"))[nn].find_all("h4"):
                                u = g.text.replace("\n","") 
                                # print(u)
                                sp = "https://5bestincity.com" + g.find("a")["href"]
                                # print(sp)
                                links1.append(sp)
     ###                       

                                r = requests.get(sp)
                        
                                soup2 = bs(r.text, "html.parser")
                                in5 = soup2.find_all("h3", class_="notranslate")
                                in6 = soup2.find_all("span", class_="rating-star")
                                                                
                                for name,rate in zip(in5,in6):
                                    name1 = name.text.replace("\n","")

                                    rate1 = rate.text  
                                    #print(rate1)
                                    #abc = rate1.replace("\n","Hello")#.split("Hello")[1]
                                    rate7 = rate1.split("\n")[1]
                                    #print(abc)
                                    rate3 = rate1.split("\n")[-2]
                                    rate3 = rate3.replace("(","").replace(")","")
                                    print(name5)
                                    city_name.append(name5)
                                    
                                    z = n[nn].text.replace("\n","")
                                    print(z)
                                    category_list.append(z)
                                    
                                    print(sp)

                                    print(u)
                                    business_list.append(u)

                                    print(name1)
                                    businessman_list.append(name1)

                                    print(rate7)
                                    rate_list.append(rate7)

                                    print(rate3) 
                                    review_list.append(rate3)
                                    

                                    print("\n")

print(len(city_name))
print(len(category_list))
print(len(business_list))
print(len(businessman_list))
print(len(rate_list))
print(len(review_list))

df = pd.DataFrame({"City":city_name,"Business Category":category_list,"Business":business_list,"Name":businessman_list,"Rate":rate_list,"Review":review_list})

print(df)

df.to_csv("5BestinCity.csv")
