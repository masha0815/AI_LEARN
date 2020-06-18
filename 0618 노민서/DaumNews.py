
# https://news.v.daum.net/v/20200618132403197
# <h3 class="tit_view" data-translation="true">"아이가 무슨 죄" 동거녀와 다툰 뒤 2살 아들 안고 분신(종합)</h3>

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://news.v.daum.net/v/20200618132403197"

html = urlopen(url) # 연결작업
html_doc = html.read()  # 문서읽기

bsObj = BeautifulSoup(html_doc, 'html.parser')  # 파싱
title = bsObj.find("h3", {"class":"tit_view"})
print("기사 제목 : ", title.text)

section = bsObj.find("section")
print(section)

pList = section.findAll("p")
for ptag in pList:
    print(ptag.text)

# dmcf-pid : 퍼블리셔가 만든 속성
p = section.find("p", {"dmcf-pid":"jLc7y6Ce5e"})
print("***")
print(p)

print("#######################################")

url = "https://news.v.daum.net/v/20200618163011900"

html = urlopen(url) 
html_doc = html.read() 
# <h3 class="tit_view" data-translation="true">여름 수박에 랩 씌우면..세균 최대 3000배 폭발</h3>
bsObj = BeautifulSoup(html_doc, 'html.parser') 
title = bsObj.find("h3", {"class":"tit_view"})
print("기사 제목 : ", title.text)



section = bsObj.find("section")
print(section)

pList = section.findAll("p")
for ptag in pList:
    print(ptag.text)

p = section.find("p", {"dmcf-pid":"jnyVIIeZ9O"})
print("***")
print(p)

