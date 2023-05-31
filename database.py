import pyrebase
import firebase
import firebase_admin
from firebase_admin import credentials,initialize_app
from firebase_admin import storage
import json
import uuid



class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
            firebase = pyrebase.initialize_app(config)
            storage=firebase.storage()
            self.db = firebase.database()
            
            cred = credentials.Certificate("./authentication/service_accout_key.json")
            firebase_admin.initialize_app(cred, {'storageBucket': 'sideaffect-2d9e7.appspot.com'})
              

    def insert_user(self,data,pw,skill,role):
        
        user_info = {
            "nickname":data['nickname'],
            "id": data['id'],
            "pw": pw,
            "phone":data['phone'],
            "interest": skill,
            "role": role
            
        }

        # 사용자 정보를 Firebase Realtime Database에 저장하는 로직 작성
        if self.user_duplicate_check(str(data['id'])):
                self.db.child("user").child(data['id']).set(user_info)
                
                print(data)
                print(role)
                print(skill)
                return True

        else:
            return False
        
            
    def user_duplicate_check(self, id_string):
        users = self.db.child("user").get()
        
        print("users###", users.val())
        if str(users.val()) == "None": # first registration
            return True
        else:
            for use in users.each():
                value = use.val()
        
                if value['id'] == id_string:
                    return False
            return True
        
    
        
    """로그인"""
    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        target_value=[]
        for use in users.each():
            value = use.val()
                
            if value['id'] == id_ and value['pw'] == pw_:
                return True
            
        return False
    
    def push_matching(self, direct_name, m):
        match = {
            # 'direct_name':direct_name,
            'id':m,
            # 'id1':m[1],
            # 'id2':m[2],
            # 'id3':m[3],
            # 'id4':m[4],
            # 'id5':m[5],
            # 'id6':m[6],
            # 'id7':m[7],
            # 'id8':m[8],
            # 'id9':m[9],
            # 'id10':m[10],
            # 'id11':m[11],
            # 'id12':m[12],
            # 'id13':m[13],
            # 'id14':m[14],
            # 'id15':m[15],
            # 'id16':m[16],
            # 'id17':m[17],
            # 'id18':m[18],
            # 'id19':m[19],
            # 'id20':m[20],
            # 'id21':m[21],
            # 'id22':m[22],
            # 'id23':m[23],
            # 'id24':m[24],
            # 'id25':m[25],
            # 'id26':m[26],
            # 'id27':m[27],
            # 'id28':m[28],
            # 'id29':m[29],
        }
        # self.db.collection(u'matching').document(direct_name).set(match,merge=True)
        self.db.child("matching").child(direct_name).push(match)
        return True
        
    
    
    
    def insert_newproject(self,pro_name,direct_name,data,project_topic):

        project_info ={
                "pro_name":pro_name,
                "direct_name":direct_name,
                "platform":data['platform'],
                "how_place":data['how_place'],
                "place":data['place'], 
                "time":data['time'],
                "desc2_overall":data['desc2'],
                "desc1_num":data['desc1'],
                "environment":data["environment"],
                "project_topic":project_topic,
                "url_site":data['url_site'],
                "hash":data['hash']
            
              
                }
        # project=data['pro_name']
        
        if self.project_duplicate_check(pro_name):
                self.db.child("project").child(direct_name).set(project_info)
                return True
        else:
            return False
        
            
    def project_duplicate_check(self,pro_name):
        
        projects = self.db.child("project_name").get()
        print("프로젝트 이름 중복 시작")
        
        if projects.val() is None: #데이터베이스가 아예 비어있는 경우
            print("프로젝트db에 아무것도 없다")
            return True # ->바로 등록 가능
        else:
            for pro in projects.each():
                print("루프ㄱ")
                print(pro.key())
                if pro.val()['pro_name'] == pro_name:
                    return False #동일한 이름이 있다 -> 등록 불가
                   
            print("루프끝, 같은 이름 없음")    
            return True    
    #-> 등록 가능
    
    #기획안 받아오기
    def post_list(self):
        post_lists = self.db.child("project").get().val()
        return post_lists
    

    
    def get_detail_byproname(self, pro_name):
        projects=self.db.child("project").get()
        target_value=""
        
        for pro in projects.each():
            value = pro.val()
                
            if value['pro_name'] == pro_name:
                target_value=value
        return target_value
    
    def matching_byname(self, direct_name):
        matchings=self.db.child("matching").get()
        target_value=""
        
        for match in matchings.each():
            value = match.val()
                
            if value['direct_name'] == direct_name:
                target_value=value
        return target_value

    

    def get_post_list(self):
        post_list= self.db.child("project").get().val()
        print("get_psot함수값")
        return post_list

        
    
    # def get_project_info(direct_name):
    # ref = db.reference("project").child(direct_name)
    # project_info = ref.get()
    # return project_info

    
    # def get_projects(self):
        
    #     pro_detail=self.db.child("project").get().val()
    #     print("내용")
    #     return pro_detail
    
    # def get_projects_byname(self,pro_name):
    #         pro_detail=self.db.child("project").get()
    #         target_value=""
    #         for proj in project.each():
    #             value=proj.val()
                
    #             if value['pro_name']==pro_name:
    #                 target_value=value
    #         return target_value
             
            
            
            
            
    
        

