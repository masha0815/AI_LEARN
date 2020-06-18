from urllib.request import urlopen

# 문서 요청 시 상태 정보의 숫자
# 200 : 성공적
# 404 : 문서 없음 - url 오류
# 500 : 사이트 오류

url = "http://www.pythonscraping.com/exercises/exercise1.html"
html = urlopen(url)
s = html.read()
print(s)

# 파싱용 라이브러리
from bs4 import BeautifulSoup
bs = BeautifulSoup(s) # html 문서를 전달하면서 객체 생성하기 - 파싱 완료

print("파싱하기")
div = bs.findAll("div") # 배열로 받아온다.
print(div[0].text)