<<<<<<< HEAD
#IT PROJECT(YEAHCHERRY)
=======
# SWTeamProject
IT side project를 위한 팀 매칭 서비스  
<br></br>
## 📍Front-End
  프로젝트 팀 매칭 Web App 구현 
 ###   Environment 
 - Node.js(v.18.12.1)
 - Npm(8.19.2)
 ### 디자인 리소스
 - Icon : Google Material Icons
 - UI 디자인 시안 : Adobe XD
 ### 화면 구현 및 시나리오
 - 메인화면
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/16ae5019-5cd4-4544-b9fa-cd2256b2063d)
 - 로그인 / 회원가입
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/4c21cc18-4f3d-4501-a5a2-91a947a2f591)
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/7fd009f1-22b4-4a5b-982f-f9c3a8073388)
 - 프로젝트 등록
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/0364e802-35c6-450d-b0df-a51e4da36421)
 - 프로젝트 등록 후 팀원 매칭
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/f0b4865e-7848-49d1-884a-011d717ecad0)
 - 팀원 이력서 확인 -> 수락시 최종매칭 완료
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/3b62e092-a940-4604-a7ee-6a12ce881370)
 



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
