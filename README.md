
# SWTeamProject
IT side project를 위한 팀 매칭 서비스: SIDE:)AFFECT

<br>

## 📍Front-End
  프로젝트 팀 매칭 Web App 구현 
 ###   Environment 
 - Node.js(v.18.12.1)
 - Npm(8.19.2)
 ### 디자인 리소스
 - Icon : Google Material Icons
 - UI 디자인 시안 : Adobe XD
 ### 화면 구현
 - 메인화면
 <img src="https://img1.daumcdn.net/thumb/R1280x0/scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F0RDKC%2FbtsiadvaypA%2FPNrN7SO0hSdFYgcXogHXsk%2Fimg.png" width="800" height="500" />
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/16ae5019-5cd4-4544-b9fa-cd2256b2063d)
 - 로그인 / 회원가입
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/4c21cc18-4f3d-4501-a5a2-91a947a2f591)
 ![image](https://github.com/YEAHCHERRY/SWTeamProject/assets/114209093/7fd009f1-22b4-4a5b-982f-f9c3a8073388)




## 📍 Backend

 **Python Flask 이용**
 
 
 **DATABASE: Firebase- Realtime database**

주요기능:

**1)회원가입 시 데이터 Firebase에 올리기**
-> 관심분야의 경우 list 의 형태로 데이터베이스에 push하여 추후에 팀원 매칭을 할 때 관심분야를 우선시하여 매칭될 수 있게 함
-> 회원정보가 저장될때 USER의 ID로 저장되게함
-> 비밀번호의 경우 보안목적으로 인해 "hash"처리함
-> 프론트엔드 페이지 "HOMEPAGE->SIGNIN->SIGNUP" 가는 과정 라우팅

**2)로그인 구현**
->DATABASE에 들어간 ID와 비밀번호가 일치하는 지 확인
->만약 일치하지 않는다면 다시금 로그인 페이지로 routing
->로그인이 된다면 HOME 화면으로 돌아가게 함

**3)기획안 올리기**
-> 기획하고자 하는 내용을 올리는 과정에서 해당 내용이 "기획자가 로그인한 ID"로 DB에 저장되게 했음
-> 복수로 처리되는 것은 list 형태로 넣어줌

**4)매칭 추천 보여주기**
->기획안이 올라가면 로그인된 아이디와 일치하는 DB의 데이터를 가져옴

**5)프로젝트 틍록시 list형태로 "프로젝트 더보기"로 보여주기**
-> HOME 페이지 밑에 "프로젝트 더보기" routing 과정 후 기획자가 기획안을 올리기만 해도 list에서 
이를 확일 할 수 있음

**6)프로젝트 마다의 세부사항 보여주기**
->Project_list 로 들어가 각각의 프로젝트를 보기위해서 "더보기" 버튼을 누르면 기획자가 올린 프로젝트를
한 눈에 확인 할 수 있도록 정보를 가져옴


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
* python 3.8.10
* selenium 3.14.1
* chrome 108.0.5359.94 ver. with ChromeDriver108.0.5359.71
* 기타 설정 : 로켓펀치 ID, PW 작성한 2 lines txt file (RocketPunch_IDPW.txt), code내 chrome driver 경로 설정  

### 2. DL Model  
koBERT.ipynb: Data preprocessing, model training & test
### Environment  
* python 3.8.10
* pandas 1.14.0
* datasets 2.7.1
* scikit-learn 1.2.0
* transformers 4.8.1
