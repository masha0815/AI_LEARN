url = "http://www.pythonscraping.com/exercises/exercise1.html"

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import sys

def getTitle( url ):
    try:
        html = urlopen(url)
        doc = html.read()
    except HTTPError as e:
        print(e)
        return None # 전달해줄 값이 없다.

    try:    
        bsObj = BeautifulSoup(doc, 'html.parser')
        title = bsObj.body.h1   # 계층형으로 body 태그 내의 첫번째 h1 태그 지정
        return title
    except AttributeError as e:
        return None 

title = getTitle( url )
if title == None:
    print("Title cannot be found")
else:
    print(title.text)

print( getTitle(url) )




