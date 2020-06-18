# 데이터가 있는 사이트부터 찾아야 합니다.
# 찾은 사이트에서 소스보기를 해서 소스에서 데이터를 검색해본다.
# 만약 있다면 requests 모듈을 통해 요청해서 bs4로 분석한다.

# 만약 없다면 iframe을 찾는다. iframe의 src 속성에 명시되어 있는 주소를 직접 요청해본다.
# 여기서 찾았다면 해당 주소로 요청해서 분석한다.

# 만약 iframe이 없다면 selenium을 통해 요청해서 bs4로 분석한다.

import requests
import bs4
import time

# 페이지를 요청한다.
def requestPage(url) :
    # 요청
    response = requests.get(url)
    # print(response.text)
    return response.text

def getData(html) :
    # 분석한다.
    soup = bs4.BeautifulSoup(html, 'lxml')
    # print(soup.prettify())

    # 140자평 데이터가 있는 li 태그들을 가져온다.
    li_list = soup.select('body > div > div > div.score_result > ul > li')

    for area1 in li_list :
        # 140자평 전체 하나를 가져온다.
        # area1 = soup.select_one('body > div > div > div.score_result > ul > li:nth-child(5)')

        # 별점
        star_score = area1.select_one('div.star_score > em')
        # print(star_score.text.strip())

        # 평가글
        rating_str = area1.select_one('div.score_reple > p > span:nth-child(2)')
        if rating_str == None :
            rating_str = area1.select_one('div.score_reple > p > span')

        # print(rating_str.text.strip())

        # 작성자
        rating_user = area1.select_one('div.score_reple > dl > dt > em:nth-child(1) > a > span')
        # print(rating_user.text.strip())

        # 작성시간
        rating_date = area1.select_one('div.score_reple > dl > dt > em:nth-child(2)')
        # print(rating_date.text.strip())

        # 저장
        with open('movie.csv', 'at', encoding='UTF-8') as fp :
            a1 = star_score.text.strip()
            a2 = rating_str.text.strip()
            a3 = rating_user.text.strip()
            a4 = rating_date.text.strip()
            fp.write(f'{a1},{a2},{a3},{a4}\n')

# 다음 페이지가 있는지 체크하는 함수
def checkNextPage(html, page) :
    soup = bs4.BeautifulSoup(html, 'lxml')
    next = soup.select_one(f'#pagerTagAnchor{page} > em')
    return next


    # test1 = soup.select_one('#pagerTagAnchor139 > em')
    # print(test1)

page = 1

while True :
    # 딜레이
    time.sleep(1)

    url = f'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=179518&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}'

    html = requestPage(url)
    getData(html)
    # 페이지 번호를 증가시키고 다음 페이지가 있는지 검사한다.
    page = page + 1
    chk = checkNextPage(html, page)
    if chk == None :
        print('수집완료')
        break
    else :
        print(f'{page}수집 중')



