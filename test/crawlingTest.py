import urllib.request
import urlopen
import re
from bs4 import BeautifulSoup

import csv

#영화 코드 추출(url입력시 영화코드 추출)
def getCode(URL):
    code_st = re.search('code=[0-9]+',URL).group()
    #입력된 url에서 code로 시작해서 숫자로 끝나는 항목을 얻어옴
    code = re.search('[0-9]+',code_st).group()
    #입력된 url에서 숫자의 형태로 되어있는 항목을 얻어옴
    return(code)

#영화 리뷰 추출(영화 code입력 시, 영화 리뷰페이지에서 평점,리뷰,날짜를 얻어옴)
def getReviewResult(CODE,CONTENT):

    page=int(1)
    #page값이 str로 들어가면 연산이 안되므로 int형변환

    count = 10
    acount = 0
    reviewArray = []
    rev = []
    i = 0
    #페이지별 리뷰 반복 가져오기
    while CONTENT:
        page=int(page)
        
        URL = url1+CODE+url2+str(page)
        #네이버 영화 리뷰페이지 전체url
        request = urllib.request.Request(URL)
        opener = urllib.request.build_opener()
        open= opener.open(request)

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
            reviewArray.insert(i,reple)
            reviewArray.insert(i+1,score)
            #print(reple)
            #print(score)

            acount += 1
            
        page += 1
        if page > round(int(CONTENT)/10):
        #if acount >= int(CONTENT):#CONTENT에 도달하면 break
            #CONTENT -> 10으로 바꿔 테스트
            return(reviewArray)
            break


def getContent(CODE):
        page=int(1)
        URL = url1+CODE+url2+str(page)
        #네이버 영화 리뷰페이지 전체url
        request = urllib.request.Request(URL)
        opener = urllib.request.build_opener()
        open= opener.open(request)
        html = open.read().decode('utf-8')

        soup = BeautifulSoup(html,"lxml")
        
        score_result = soup.find('div',class_='score_total')
        strong = score_result.find('strong',class_='total')
   
        ems = strong.find_all('em')
        content = ems[1].get_text()
        content = content.replace(",","")
        #쉼표제거 ex)9,439 -> 9439
        #print(content)
        return(content)

def writeCsv(c):
    f = open('review.csv', 'w', newline='')
    wr = csv.writer(f)
    
    for i in range(1,len(c),2):
        
        wr.writerow([c[i-1],c[i]])

    f.close()
url1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code='
url2 = '&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='
URL = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=75006'
#영화 url입력
code = getCode(URL)
content = getContent(code)
print("crawling...")
c = getReviewResult(code,content)
#print(c)
print("csv writing...")
writeCsv(c)


            
