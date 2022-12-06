import os
from time import sleep
import time
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def profile_crawl(j):
    name_css = '#people-header > div.content > div > div.nowrap.name' # 이름
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, name_css)))
    name = driver.find_element(By.CSS_SELECTOR, name_css).get_attribute('innerText')

    interest_xPath = '//*[@id="pro-of"]' # 관심분야
    try:
        interest = driver.find_element(By.XPATH, interest_xPath).get_attribute('innerText')
    except NoSuchElementException:
        interest = ''

    intro_xPath = '//*[@id="people-overview"]' # 소개
    try:
        intro = driver.find_element(By.XPATH, intro_xPath).get_attribute('innerText')
    except NoSuchElementException:
        intro = ''

    car_xPath = '//*[@id="people-career"]' # 경력
    try:
        car = driver.find_element(By.XPATH, car_xPath).get_attribute('innerText')
    except NoSuchElementException:
        car = ''

    proj_xPath = '//*[@id="people-project"]' # 프로젝트
    try:
        proj = driver.find_element(By.XPATH, proj_xPath).get_attribute('innerText')
    except NoSuchElementException:
        proj = ''

    field_xPath = '//*[@id="people-specialty"]' # 활동분야
    try:
        field = driver.find_element(By.XPATH, field_xPath).get_attribute('innerText')
    except NoSuchElementException:
        field = ''
    driver.back()

    # 문자열 안에 \n가 있다면 ' '로 바꿔주기
    if(interest.find('\n')!=-1): 
        interest = interest.replace('\n',' ')
    if(intro.find('\n')!=-1): 
        intro = intro.replace('\n',' ')
    if(car.find('\n')!=-1): 
        car = car.replace('\n',' ')
    if(proj.find('\n')!=-1): 
        proj = proj.replace('\n',' ')
    if(field.find('\n')!=-1): 
        field = field.replace('\n',' ')

    # 문자열 안에 `(구분자)가 있다면 '로 바꿔주기 
    if(interest.find('`')!=-1): 
        interest = interest.replace("`","'")
    if(intro.find('`')!=-1): 
        intro = intro.replace("`","'")
    if(car.find('`')!=-1): 
        car = car.replace("`","'")
    if(proj.find('`')!=-1): 
        proj = proj.replace("`","'")
    if(field.find('`')!=-1): 
        field = field.replace("`","'")
                            
    file = open(fileName, 'a', encoding='utf-8')
    file.write(name + "`" + interest + "`" + intro + "`" + car + "`" + proj + "`" + field + "\n")
    file.close()

    # # pandas에 작성
    # interest = interest+'이 있습니다.'
    # car = '경력은 '+car+' 을 해봤습니다.'
    # proj = '프로젝트는 '+proj+' 을 해봤습니다.'
    # field = field+' 분야에서 활동합니다.'


###################### main함수 ######################
fileName = 'Rocket_profile.csv'
file = open(fileName, 'w', encoding='utf-8')
file.write("관심분야`소개`경력`프로젝트`활동분야\n")
file.close()

file = open('RocketPunch_IDPW.txt', 'r', encoding='utf-8')
ID = file.readline()
PW = file.readline()

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
chromedriver_path = "C:/Users/dnflc/Downloads/selenium/chromedriver.exe"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기

driver.get('https://www.rocketpunch.com/people?job=1')  # 주소 가져오기
driver.implicitly_wait(0.5) # 기다려 주자
driver.find_element(By.XPATH, '//*[@id="main-menu"]/div[3]/a[1]').click() #로그인 페이지 이동
driver.find_element(By.NAME, 'email').send_keys(ID)
driver.find_element(By.NAME, 'password').send_keys(PW)
driver.find_element(By.XPATH, '//*[@id="form-login-inline"]/div[3]/button').click() # 로그인
driver.implicitly_wait(1) # 기다려 주자
del_element = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[2]/div[1]/a/i') # 검색 조건 조정
driver.execute_script("arguments[0].click();", del_element)
sw_element = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/div/div[2]/div[2]/a[1]') # 검색 조건 조정
driver.execute_script("arguments[0].click();", sw_element)

i=0
while True: # 페이지별 루프
    i+=1
    for j in range(1, 11): # 프로필 개수만큼 루프를 돈다.
        if i==1:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-results"]/div[1]/div[2]/div/div['+str(2*j+3)+']/div[1]/a')))
            profile = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[1]/div[2]/div/div['+str(2*j+3)+']/div[1]/a')
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-results"]/div[1]/div[2]/div/div['+str(2*j)+']/div[1]/a')))
            profile = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[1]/div[2]/div/div['+str(2*j)+']/div[1]/a')
        driver.execute_script("arguments[0].click();", profile) # 각 프로필 열기
        profile_crawl(j)
    for j in range(1, 11):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-results"]/div[3]/div/div/div['+str(2*j-1)+']/div[1]/a')))
        profile = driver.find_element(By.XPATH, '//*[@id="search-results"]/div[3]/div/div/div['+str(2*j-1)+']/div[1]/a')              
        driver.execute_script("arguments[0].click();", profile) # 각 프로필 열기
        profile_crawl(j)
    print('['+str(i)+'페이지] 완료') # ex) [1페이지] 완료
    
    if i>=500: # 500페이지가 넘으면 끝낸다
        break

    # 다음 페이지 버튼 클릭
    if i<6:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child('+str(i+1)+')')))
        next_btn = driver.find_element(By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child('+str(i+1)+')')
    elif i==499:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child(7)')))
        next_btn = driver.find_element(By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child(7)')
    else:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child(6)')))
        next_btn = driver.find_element(By.CSS_SELECTOR, '#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a:nth-child(6)')
    print(next_btn.get_attribute("innerText"))
    driver.execute_script("arguments[0].click();", next_btn)
    time.sleep(4)

print("End of Crawl")
driver.close()
driver.quit()
