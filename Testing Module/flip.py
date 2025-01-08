import requests
from bs4 import BeautifulSoup

for i in range (2,11):
    url = "https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy,4io"
    r = requests.get(url)
    print (r)

    soup =BeautifulSoup(r.text, "lxml")
    # print (soup)

    np = soup.find("a",class___="_1LKT03").get("href")
    cnp = "https://www.flipkart.com"+np
    print (cnp)

    #url = cnp
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text "lxml")