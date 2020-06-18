# web driver 부터 다운받아야 한다.
# https://pypi.org/project/selenium/

# 라이브러리 설치
# pip install selenium

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 브라우저를 실행시킨다.
driver = webdriver.Chrome('chromedriver')

# 네이버 요청한다.
driver.get('https://www.naver.com')

# 회원 가입 링크를 누른다.
link1 = driver.find_element_by_css_selector('#account > div > a')
link1.click()

# 약관 전체 동의를 누른다.
tag2 = driver.find_element_by_css_selector('#join_form > div.terms_p > p > span > label')
tag2.click()

# 확인을 누른다.
tag3 = driver.find_element_by_css_selector('#btnAgree')
tag3.click()

# 회원정보 입력
tag4 = driver.find_element_by_css_selector('#id')
tag4.send_keys('minso')

tag5 = driver.find_element_by_css_selector('#pswd1')
tag5.send_keys('asdfasdf1234')

tag6 = driver.find_element_by_css_selector('#pswd2')
tag6.send_keys('asdfasdf1234')

tag7 = driver.find_element_by_css_selector('#name')
tag7.send_keys('김정년')

tag8 = driver.find_element_by_css_selector('#yy')
tag8.send_keys('2000')

tag11 = driver.find_element_by_css_selector('#mm')
tag11_select = Select(tag11)
tag11_select.select_by_value('02')

tag9 = driver.find_element_by_css_selector('#dd')
tag9.send_keys('20')

tag12 = driver.find_element_by_css_selector('#gender')
tag12_select = Select(tag12)
tag12_select.select_by_value('F')

tag10 = driver.find_element_by_css_selector('#phoneNo')
tag10.send_keys('01012345678')


