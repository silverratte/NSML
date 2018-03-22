import urllib.request
import request
import urlopen

import re
from bs4 import BeautifulSoup

#영화 코드 추출(url입력시 영화코드 추출)
def getCode(URL):
    code_st = re.search('code=[0-9]+',URL).group()
    #입력된 url에서 code로 시작해서 숫자로 끝나는 항목을 얻어옴
    code = re.search('[0-9]+',code_st).group()
    #입력된 url에서 숫자의 형태로 되어있는 항목을 얻어옴
    return(code)

#영화 리뷰 추출(영화 code입력 시, 영화 리뷰페이지에서 평점,리뷰,날짜를 얻어옴)
def getReviewResult(CODE):
    #f=open('review_'+code+'.txt','w')
    #텍스트 파일로 저장
    page=int(1)
    #page값이 str로 들어가면 연산이 안되므로 int형변환

    #count = int(input('Page Number:'))
    #리뷰페이지 갯수 입력하기
    count = 10
    #20페이지
    
    #페이지별 리뷰 반복 가져오기
    while count:

        URL = url1+CODE+url2+str(page)
        #네이버 영화 리뷰페이지 전체url
        request = urllib.request.Request(URL)
        opener = urllib.request.build_opener()
        open= opener.open(request)
        #open = urlopen(URL)
        html = open.read().decode('utf-8')

        soup = BeautifulSoup(html,"lxml")
        
        score_result = soup.find('div',class_='score_result')
        
        lis = score_result.find_all('li')

        for li in lis:

            page = int(page)

            reple = li.find('div',class_='score_reple').find('p').get_text()
            #리뷰항목만 가져옴
            score = li.find('div',class_='star_score').find('em').get_text()
            #평점항목만 가져옴

            print(reple)
            print(score)

            #f.write('영화 평점 : '+score.encode('utf-8')+'\n')
            #f.write('리뷰 내용 : '+reple.encode('utf-8')+'\t')
            #텍스트 파일에 입력

            count-=1

            if not count:
                break
            page += 1

        #f.close()
        #열어 놓은 텍스트 파일 종료

#def getPage(CODE):
    
url1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
url2 = '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
URL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=75006'
#영화 url입력
code = getCode(URL)
getReviewResult(code)

            
