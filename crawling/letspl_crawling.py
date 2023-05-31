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

# 스크롤 끝까지 내리기
def scroll_down():
    # 현재 브라우저의 높이
    last_height = driver.execute_script(
        "return document.body.scrollHeight")  # 브라우저 높이를 확인 가능
    # 검색 화면에서 스크롤을 끝까지 내리기
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 새 스크롤 높이 계산, 비교
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                # 화면 맨 아래 펼쳐보기 버튼 클릭
                search_more = driver.find_element(
                    By.CSS_SELECTOR, ".expender.open")
                search_more.click()
                time.sleep(2)
            except:
                print("error")
                break
        last_height = new_height

def project_crawl(i):
    scroll_down()
    # i번째 프로젝트 페이지 열기
    action = ActionChains(driver)
    action.click(on_element = driver.find_element_by_xpath('//*[@id="__next"]/section/div[3]/div[3]/div[2]/div['+ str(i) +']')).perform()# 프로젝트 누르기
    # 페이지 이동
    
    name_xPath = '//*[@id="__next"]/section/div[1]/div[2]/li/div/div[2]/h2'
    title_class = 'projectTit'
    writing_sel = 'div.section.onlyTxtSection' # 모집글
    skill_sel = 'div.section.skillSection'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, writing_sel)))
    name = ''
    title = ''
    writing = ''
    skill = ''
    try:
        name = driver.find_element_by_xpath(name_xPath).get_attribute('innerText')
        title = driver.find_element_by_class_name(title_class).get_attribute('innerText')
        writing = driver.find_element_by_css_selector(writing_sel).get_attribute('innerText')
        skill = driver.find_element_by_css_selector(skill_sel).get_attribute('innerText')
    except NoSuchElementException:
        pass

    driver.back()

    # 문자열 안에 \n가 있다면 ' '로 바꿔주기
    if(title.find('\n')!=-1): 
        title = title.replace('\n',' ')
    if(writing.find('\n')!=-1): 
        writing = writing.replace('\n',' ')
    if(skill.find('\n')!=-1): 
        skill = skill.replace('\n',' ')
                            
    file = open(fileName, 'a', encoding='utf-8')
    file.write(name + '`' + title + '`' + writing + '`' + skill + "\n")
    file.close()


###################### main함수 ######################
fileName = 'letspl_project.csv'
file = open(fileName, 'w', encoding='utf-8')
file.write("이름`제목`모집글`기술스택\n")
file.close()

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')
chromedriver_path = "C:/Users/dnflc/Downloads/selenium/chromedriver.exe"
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기
driver.get('https://letspl.me/project?location=KR00&industry=00&status=00&recruting_only=true&recruting=0000&type=01')  # 주소 가져오기
driver.implicitly_wait(0.5) # 기다려 주자

scroll_down()

projects_list = driver.find_elements_by_class_name('projectGridWrap') # 프로젝트 목록 생성
for i in range(1, len(projects_list)+1): # 프로젝트 개수만큼 루프를 돈다.
    project_crawl(i)
    print(str(i)+'개 완료') # ex) 6개 완료

print("End of Crawl")
driver.close()
driver.quit()
