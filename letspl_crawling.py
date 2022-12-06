import os
from time import sleep
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def project_crawl(i):
    # i번째 프로젝트 페이지 열기
    action = ActionChains(driver)
    action.click(on_element = driver.find_element_by_xpath('//*[@id="__next"]/section/div[3]/div[2]/div['+ str(i) +']')).perform()# 프로젝트 누르기
    # 페이지 이동
    
    writing_xPath = '//*[@id="__next"]/section/div[2]/div[1]/div[2]/div/div[3]/div' # 주소
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, writing_xPath)))
    writing = driver.find_element_by_xpath(writing_xPath).get_attribute('innerText')
    driver.back()

    # 문자열 안에 \n가 있다면 ' '로 바꿔주기
    if(writing.find('\n')!=-1): 
        writing = writing.replace('\n',' ')
                            
    file = open(fileName, 'a', encoding='utf-8')
    file.write(writing + "\n")
    file.close()


###################### main함수 ######################
fileName = 'letspl_project.csv'
file = open(fileName, 'w', encoding='utf-8')
file.write("모집글\n")
file.close()

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
chromedriver_path = "C:/Users/dnflc/Downloads/selenium/chromedriver.exe"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기
driver.get('https://letspl.me/project?location=KR00&industry=00&status=00&recruting_only=true&recruting=0000&type=01')  # 주소 가져오기
driver.implicitly_wait(0.5) # 기다려 주자

projects_list = driver.find_elements_by_css_selector('#__next > section > div.projectView.projectAllGridView > div.projectGridView > div') # 프로젝트 목록 생성
for i in range(1, len(projects_list)+1): # 프로젝트 개수만큼 루프를 돈다.
    project_crawl(i)
    print(str(i)+'개 완료') # ex) 6개 완료

print("End of Crawl")
driver.close()
driver.quit()