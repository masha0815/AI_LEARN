from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.yna.co.kr/view/AKR20200618086651001?input=1195m"

html = urlopen(url) 
html_doc = html.read()  

bs = BeautifulSoup(html_doc, "html.parser")
divList = bs.findAll("div", {"class":"info_image"})
liList = divList[0].ul.findAll("li")
print(liList[0])
img = liList[0].img
print(img['src'])
html = urlopen(url)
html_doc = html.read()

bsObj = BeautifulSoup(html_doc, 'html.parser')
title = bsObj.find("h1", {"class":"tit"})
print("기사 제목 : ", title.text)




####################################

#url = "https://www.daum.net/"
#bs = BeautifulSoup(html_doc, "html.parser")
# 첫번째거 하나만 출력
#tagList = bs.find("li", {"class":"ta_txt rubics_single"})
#print( tagList.text )

# 목록 전체를 배열로 - find_all 또는 findAll
#tagList = bs.findAll("li", {"class":"ta_txt rubics_single"})
#for i in range(0, len(tagList)): #배열의 인덱스

#for item in tagList:
 #   print( item.text )



