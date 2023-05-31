<<<<<<< HEAD
#IT PROJECT(YEAHCHERRY)
=======
# SWTeamProject
IT side project를 위한 팀 매칭 서비스  
<br></br>
## 📍Front-End
- 메인화면
![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/593b694b-85a6-40a4-b8f7-5fc888ad1115)


<br></br>
## 📍Deep Learning
* 팀 매칭 기능 구현 방식 (사용자가 팀원 모집글 업로드시)
  1. 학습된 딥러닝 모델을 이용하여 모집글 embedding
  2. embedding된 vector를 기존에 embedding됐던 이력서 vector들과의 유사도를 구해 높은 순서대로 출력  

## Process 
### 1. Data Crawling  
letspl_crawling.py: 렛플에서 39건의 모집글 데이터 크롤링  
rocket_crawling.py: 로켓펀치에서 약 10,000건의 이력서 데이터 크롤링  
### Environment 
* python3  
* selenium (Install selenium: ```pip install selenium```)
* chrome 108.0.5359.94 ver. with ChromeDriver108.0.5359.71  
(Download: https://chromedriver.chromium.org/downloads)
* 기타 설정 : 로켓펀치 ID, PW 작성한 2 lines txt file (RocketPunch_IDPW.txt), code내 chrome driver 경로 설정  

### 2. DL Model  
### Environment  
* koBERT
>>>>>>> 3a963b09d02b33252178210d41718099a8f3c9fd
