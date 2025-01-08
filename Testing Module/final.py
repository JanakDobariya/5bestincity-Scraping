import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://5bestincity.com/"
r = requests.get(url)

r5 = requests.get(url)

soup5 = bs(r5.text,"html.parser")
cities5 = soup5.find_all("div",class_ = "col-lg-2 col-md-6")

name_list3 = []
sg = []
all_list = []
name15 = []
for city5 in cities5:
    text = "".join(city5.text).strip()
    link_ = city5.find('a')["href"]
    temp = {
        'name': text,
        'link': link_
    }
    all_list.append(temp)
    #print(name5)

for i in all_list:
    request_ = requests.get(i['link'])
    con = bs(request_.text, "html.parser")
    sub_list = con.find_all('ul', class_="list")
    for j in sub_list:
        pass
        j.find_all('h4')[0].text
    pass

soup = bs(r.text, "html.parser")
cities = soup.find_all("div", attrs={"class": "col-lg-2 col-md-6"})
links = []

for link,nam in zip(cities,name15):
    try:
        href = link.find("a")["href"]
    except:
        href = None
    if href:
        if r"https://5bestincity.com/businesses-in" in href:
            if href not in links:
                links.append(href)
                # print(nam,href)
                #print(href)  # Print the city link one by one
                # print(links)                # Print all city links in the list


                r3 = requests.get(href)
                soup3 = bs(r3.text, "html.parser")
                cities3 = soup3.find_all("h4")


                for city3 in cities3:
                    try:
                        name3 = city3.find("a").text
                        name3 = name3.replace("\n", "")
                        # print(name3)
                        name_list3.append(name3)
                    except:
                        pass

                # print(name_list3)

                r1 = requests.get(href)
                soup1 = bs(r1.text, "html.parser")
                cities1 = soup1.find_all("a")
                links1 = []

                for link1 in cities1:
                    try:
                        href1 = link1["href"]
                    except:
                        href1 = None
                    if href1:
                        if r"businesses" not in href1:
                            if r"-in-" in href1:
                                # print(href)
                                jd = "https://5bestincity.com" + href1
                                links1.append(jd)
                                # print(jd)

                                r = requests.get(jd)
                                sg = []
                                soup2 = bs(r.text, "html.parser")
                                in5 = soup2.find_all("h3", class_="notranslate")

                                for name in in5:
                                    name1 = name.text
                                    name1 = name1.replace("\n", "")
                                    sg.append(name1)


                                print(nam)#,href)
                                if name_list3:
                                    print(name_list3[0])
                                    for i in sg:
                                        print("-"+i)
                                    print("\n")
                                    name_list3 = name_list3[1:]



# df = pd.DataFrame({"City":links,"Business":name_list3,"Name":sg})

# print(df)

# df.to_csv("5BestinCity.csv")

