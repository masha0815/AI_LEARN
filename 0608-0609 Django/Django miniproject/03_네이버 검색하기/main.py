from selenium import webdriver

keyword = input('검색어 : ')

# 드라이버 로딩
driver = webdriver.Chrome('chromedriver')

# 네이버에 접속한다.
driver.get('https://www.naver.com')

# 검색어를 입력한다.
tag1 = driver.find_element_by_css_selector('#query')
tag1.send_keys(keyword)

tag2 = driver.find_element_by_css_selector('#search_btn')
tag2.click()

# 현재 페이지의 html 데이터를 받아온다.
html = driver.page_source
print(html)

# 이후로는 bs4를 통해 데이터를 분석해서 가져오면 된다.
# selenium 자체에도 데이터를 가져오는 기능이 있다.
# 이걸 이용하는 것을 추천한다.


