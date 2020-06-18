# 로컬 경로에서 html 문서를 읽어 파싱하기
from bs4 import BeautifulSoup

html_doc = open("./test2.html", encoding="utf8")
s = html_doc.read()
print(s)

# 파싱 - 읽어들인 xml 문서를 BeautifulSoup 객체에 전달한다.
bs = BeautifulSoup(s) # 객체 생성 - bs가 문서를 읽어 파싱한 정보를 가지고 있다.

# 태그명만 주면 첫번째 데이터 하나만 찾는다.
h1 = bs.find("h1")
print(h1) # h1 객체 자체(태그 포함)을 출력한다.
print(h1.text) # 태그를 제외한 텍스트만 출력한다. 

# 태그로 접근하기 - find, find_all 태그명
# 같은 태그가 여러 개 있을 때 배열로 찾는 방법 - find_all
hList = bs.find_all("h1")
print(hList[0].text)
print(hList[1].text)
print(hList[2].text)

for title in hList:
    print(title.text)

p = bs.find("p")
print("p", p.text)

# 모든 태그에는 id, class 속성이 있다.
# id - 한 페이지에서 id는 중복되면 안 된다. javascript에서 태그에 접근할 때 이 속성의 값을 이용해서
#      접근하는데, 중복이 되면 접근을 할 수가 없다.
# class - 여러 개의 태그가 동일한 클래스명을 소유할 수 있다.
#         배열의 형태이며 보통 화면에 디자인을 넣기 위해 사용한다.
# input, textarea 태그는 별도로 name 속성을 가질 수 있는데 name 속성에 값을 담아 서버로 전송할 때 쓴다.
# html 파싱 시 태그뿐만 아니라 이 세 개의 속성을 이용해 값을 적당하게 가져올 수 있다.

# 첫번째 인자로 태그명, 두번째 인자로 id 속성명
tag = bs.find("h1", id="blue1")
print(tag.text)

tag = bs.find("h1", id="blue2")
print(tag.text)

for i in range(1, 3):
    tag = bs.find("h1", id="red"+str(i))
    print(tag.text)

# class 속성 사용 시 find_all 사용
tags = bs.find_all("h1", class_="blueclass")
for tag in tags:
    print(tag.text)

# 파라미터를 dict 타입으로 전달
tags = bs.find_all("h1",{"class":"blueclass"})
for tag in tags:
    print(tag.text)

id = bs.find("h1", {"id":"red1"})
print(id.text)

# ul 태그에 대한 참조를 먼저 얻는다.
ul1 = bs.find("ul", {"class":"coffee"})
print(ul1.find("li").text)
for li in ul1.findAll("li"):
    print(li.text)






