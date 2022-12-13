
# SWTeamProject
IT side project를 위한 팀 매칭 서비스
<br />
## 📍Front-End
  IT side project 매칭 Web App 구현 
 ###  ● Process(개발환경 : Node.js)
1. main 페이지 index.html, main.css, main.js 작성
2. signin 로그인 페이지 index.html, signin.css, signin.js 작성
3. main, signin 공통으로 적용되는 css는 common.css에서 관리
4. main, signin 공통으로 적용되는 js는 common.js에서 관리
5. main, signin 페이지 연결 -> main 페이지 상단의 메뉴에서 Sign In 클릭하면 sinin 페이지로 전환
<br />



## 📍Deep Learning
* 팀 매칭 기능 구현 방식 (사용자가 팀원 모집글 업로드시)
  1. 학습된 딥러닝 모델을 이용하여 모집글 embedding
  2. embedding된 vector를 기존에 embedding됐던 이력서 vector들과의 유사도를 구해 높은 순서대로 출력  

## Process 
### 1. Data Crawling  
letspl_crawling.py: 렛플에서 39건의 모집글 데이터 크롤링  
rocket_crawling.py: 로켓펀치에서 약 10,000건의 이력서 데이터 크롤링  
### Environment 
* python 3.8.10
* selenium 3.14.1
* chrome 108.0.5359.94 ver. with ChromeDriver108.0.5359.71
* 기타 설정 : 로켓펀치 ID, PW 작성한 2 lines txt file (RocketPunch_IDPW.txt), code내 chrome driver 경로 설정

### 2. Model Training  
크롤링한 데이터를 koBERT 모델에 학습
### Environment  
* python 3.8.10
