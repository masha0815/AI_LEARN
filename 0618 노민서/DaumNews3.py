from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse    # 한글 깨짐 해결

search = "&q=" + parse.quote_plus("코로나")

for i in range(1, 6):
    page = "&page="+str(i)  # i = int 타입 -> str 타입으로 전환

    url = "https://m.search.daum.net/search?w=news&DA=PGD&n=15" + search + page
    print(url)

    html = urlopen(url) 
    html_doc = html.read()  
    # print(html_doc)
    bs = BeautifulSoup(html_doc)
    div = bs.find("div", {"class":"compo-fulltext ty_tit2"})
    liList = div.ul.findAll("li")
    for item in liList:
        print(item.find("strong", {"class":"tit-g"}).text)


# 과제
# https://www.ilifo.co.kr/boards/chunsik?page.page=1&searchType=title&searchWord=




