from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ilifo.co.kr/center"

html = urlopen(url) 
html_doc = html.read()  

bs = BeautifulSoup(html_doc, "html.parser")
divList = bs.findAll("div", {"class":"info_image"})
liList = divList[0].ul.findAll("li")
for li in liList:
    img = li.img
    print(img['src'])