from flask import Flask, render_template, request, redirect, flash, url_for, session
from database import DBhandler
import hashlib
import sys
import math
import firebase
import firebase_admin
from firebase import firebase
from subprocess import call
from flask_socketio import SocketIO, send
from sentence_transformers import SentenceTransformer
import MDS
from firebase_admin import credentials, storage
from firebase_admin import firestore
import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

application = Flask(__name__)
DB = DBhandler()
application.secret_key = 'super secret key'
application.config['SESSION_TYPE'] = 'filesystem'


#딱 들어가면 나오는 페이지
@application.route("/") 
def hello():
    return render_template("index.html")
    
@application.route("/index") 
def main():
    return render_template("index.html")

@application.route("/uploadpdf") 
def uploadpdf():
    return render_template("uploadpdf.html")


@application.route("/userdetail1") 
def userdetail1():
    return render_template("userdetail1.html")

@application.route("/userdetail2") 
def userdetail2():
    return render_template("userdetail2.html")

@application.route("/userdetail3") 
def userdetail3():
    return render_template("userdetail3.html")

@application.route("/userdetail4") 
def userdetail4():
    return render_template("userdetail4.html")


@application.route("/uploadpdf_post") 
def uploadpdf_post():
    return render_template("index.html")

#새로운 프로젝트
@application.route("/newproject")
def newproject():
    
    model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

    return render_template("newproject.html")
    

#로그아웃
@application.route("/logout")
def logout_user():
    
    session.clear()
    return redirect(url_for('hello'))

#기획안 받기
@application.route("/newproject_register",methods=['POST'])
def create_course():
    
    global idx
    if request.method=='POST':
        
        data=request.form
        pro_name=request.form['pro_name']
        direct_name=session['id']
    
        project_topic=request.form.getlist('project_topic')
        
    if DB.insert_newproject(data['pro_name'],direct_name,data,project_topic):
        m = MDS.MDS_new(model, pro_name, data['desc1'], data['desc2'])
        for i in range(len(m)):
            if DB.push_matching(direct_name, m[i]):
                print(str(i)+'번째 DB ok')
            else:
                print(str(i)+'번째 DB 올리기 실패')
        # DB.search_push_user(direct_name, m0)
        # DB.search_push_user(direct_name, m1)
        # DB.search_push_user(direct_name, m2)
        # DB.search_push_user(direct_name, m3)
        # DB.search_push_user(direct_name, m4)
        # return render_template("index.html",data=data)
        return render_template("recommenduser.html",data=data)
    

#회원가입
@application.route("/sign-up")
def signup():
    return render_template("sign-up.html")
 

#회원가입 시 입력
@application.route('/sign-up_post', methods=['POST'])
def insert_user():
    data=request.form
    skill=request.form.getlist('mycheckbox')
    role=request.form.getlist('myrole')
    print(skill)
    print(role)
    print(data)
    
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    
    if DB.insert_user(data,pw_hash,skill,role):
         return redirect(url_for('hello'))
        
    else:
        flash("이미 존재하는 아이디입니다!")
        return render_template("sign-up.html")
        
#로그인              
@application.route("/sign-in")
def login():
    return render_template("sign-in.html")


@application.route("/login_confirm", methods=['POST'])
def login_user():
    id_=request.form['id']
    pw=request.form['pw']
    pw_hash = hashlib.sha256(pw.encode('utf-8')).hexdigest()
    
    if DB.find_user(id_,pw_hash):
        session['id']=id_
        print("okok")
        return redirect(url_for('hello'))
    
    else:
        flash("아이디와 비밀번호를 다시 확인해주세요!")
        return render_template("sign-in.html")
    
#더보기 후 나오는 project list
@application.route("/post_list") 
def list_restaurants():
     data=DB.get_post_list()
    
     return render_template("post_list.html",datas=data.items())   
      
# @application.route("/newpdf_register",methods=['POST'])
# def newpdf_register():
#     print("되고있나요")
#     return render_template("index.html")

    
 #더보기 후 나오는 project list
@application.route("/projectDetail/<pro_name>/") 
def view_pros(pro_name):
     data1=DB.get_detail_byproname(str(pro_name))
    
    
    
     return render_template("projectDetail.html",datas=data1)    
    
#아이디추천
@application.route("/recommenduser/<direct_name>/")
def recommend_user(direct_name):
    data1 = DB.matching_byname(str(direct_name))
    return render_template("recommenduser.html", datas=data1.items())
       
             
if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True);

