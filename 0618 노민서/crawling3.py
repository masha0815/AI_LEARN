from bs4 import BeautifulSoup

html_doc = open("./test3.html", encoding="utf8")
s = html_doc.read()

bs = BeautifulSoup(s)

table = bs.find("table")
# print(table)

#thead 쪽에 있는 제목들
thead = table.find("thead")
print(thead)

th = thead.findAll("th")
print(th[0].text)
print(th[1].text)
print(th[2].text)

tbody = table.find("tbody")
trList = tbody.findAll("tr") #배열
for tr in trList:
    tdList = tr.findAll("td")
    for td in tdList:
        print(td.text, end=" ")
    print()





