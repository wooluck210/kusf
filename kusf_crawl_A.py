# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)
# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import xlsxwriter
import re

chrome_options = Options()
chrome_options.add_argument("--headless")

# 엑셀 처리 선언. 엑셀 켜기
workbook = xlsxwriter.Workbook("C:/Users/freew/data/kusf_result_A.xlsx")
# 워크 시트. 시트 여러 개 생성 가능
worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

# webdriver 설정(Chrome, Firefox 등) - Headless 모드
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정(Chrome, Firefox 등) - 일반 모드
#browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)  # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://www.kubf.or.kr/record/attack.php')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 대학농구리그 클릭
WebDriverWait(browser, 3) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctview"]/div[2]/form/select[1]/option[2]'))).click()

# 리그연도 클릭
WebDriverWait(browser, 3) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctview"]/div[2]/form/select[2]/option[2]'))).click()

# 성별 클릭
WebDriverWait(browser, 3) \
    .until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="ctview"]/div[2]/form/select[3]/option[2]'))).click()

time.sleep(2)
# 현재 페이지
cur_page_num = 2
# 크롤링 페이지 수
target_crawl_num = 10
row = 0
col = 0
while cur_page_num <= target_crawl_num:

    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 기록표 선택(리스트)
    # re 로 태그 내용만 빼오는 방법
    #A_record_table = str(soup.select('table.tableline.W100P > tbody > tr')) # 띄어쓰기 사이에 점 찍기
    A_record_table = soup.select('table.tableline.W100P > tbody > tr') # 띄어쓰기 사이에 점 찍기


    # 2019 부분별 순위표 목록
    # elm = browser.find_element(By.CLASS_NAME, 'H30')
    # print("순위표 목록:", elm)
    # print(A_record_table)


    for v in A_record_table:
        col = 0
        if v.select('td'):
            for i in range(1, 15):
                con = v.select('td:nth-child(%s)' % i)[0].text
                worksheet1.write(row, col, con)
                col += 1
            row += 1
        else :
            pass

    # 페이지 증가
    cur_page_num += 1
    if cur_page_num > target_crawl_num:
        print('Crawling Succeed.')
        break
    # 페이지 이동 클릭
    WebDriverWait(browser, 3) \
        .until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="ctview"]/div[2]/form/select[2]/option[{}]'.format(cur_page_num)))).click()
    # 성별 클릭
    WebDriverWait(browser, 3) \
        .until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ctview"]/div[2]/form/select[3]/option[2]'))).click()

# BeautifulSoup 인스턴스 삭제
del soup

# 브라우저 종료
browser.quit()

# 엑셀 파일 닫기
workbook.close()