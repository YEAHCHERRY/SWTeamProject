import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os  # for os.path.basename
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.manifold import MDS
from scipy.spatial import distance
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import olefile
import zlib
import struct
from numpy import dot
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer

# 특수문자 제거
def sub_exc(text):
    pattern = re.compile(r'[^\w\s]')
    text_rm = pattern.sub('', text)
    if(text_rm.find('\n')!=-1): 
        text_rm = text_rm.replace('\n',' ')
    return text_rm

# 이력서 데이터 load
def load_data():
    frame = pd.read_pickle('data/frame.pkl')
    return frame

# 유사도 계산 함수
def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

# desc1에 기술스택이 존재하는지 여부 판단하는 함수
def has_skill(desc1, frame, t): # desc1은 모집글의 모집부문 또는 이력서 글 전체 / frame은 이력서 데이터 또는 모집글 데이터 
    wordframe_path = 'data/ITword.csv'
    wordframe = pd.read_csv(wordframe_path, encoding='utf-8')
    
    # 해당 글에 어떤 ITword들이 있는지 확인
    want_num = []
    for i in range(len(wordframe)):
        if(desc1.lower().find(wordframe.loc[i, 'words'])!=-1):
            want_num.append(i)
            
    # 사용자가 모집글을 올렸을 경우
    if t==0:
        # frame에서 해당 기술스택을 가진 이력서들만 출력
        for i in range(len(frame)):
            for j in range(len(want_num)):
                wo = (wordframe[wordframe['stem']==wordframe.loc[want_num[j], 'stem']])['words']
                if(not any(w in frame.loc[i, '글'].lower() for w in wo)): # 요구하는 기술스택 중 하나라도 없는 이력서들 삭제
                    frame.drop([i], axis=0, inplace=True)
                    break
        frame = frame.reset_index(drop=True)
        
    # 사용자가 이력서를 올렸을 경우
    elif t==1:
        for i in range(len(frame)):
            for j in range(len(want_num)):
                wo = (wordframe[wordframe['stem']==wordframe.loc[want_num[j], 'stem']])['words']
                if(not any(w in frame.loc[i, '글'].lower() for w in wo)): # 보유한 기술스택 중 일부도 없는 모집글들 삭제
                    frame.drop([i], axis=0, inplace=True)
                    break
        frame = frame.reset_index(drop=True)
        
    return frame


### 사용자가 이력서를 등록했을 때 ###
def afterupload(model, ID, file_path):
    try:
        if(file_path[-3:]=='pdf'):
            text = get_pdf_text(file_path)
        elif(file_path[-4:]=='docx'):
            text = get_docx_text(file_path)
        elif(file_path[-3:]=='hwp'):
            text = get_hwp_text(file_path)
        
        text = sub_exc(text)
        
        new_data = {
            'ID' : ID,
            '글' : sub_exc(text),
            '종류' : 0,
            'embedding' : model.encode(text)
        }
        frame = load_data()
        frame = frame.append(new_data, ignore_index=True)
        return True
    except:
        return False

    
### 사용자가 모집글을 등록했을 때 ###
def MDS_new(model, pro_name, desc1, desc2):
    na = pro_name
    wr = sub_exc(desc2)
    ty = 1
    frame = load_data()  # 데이터 로드
    
    t = 1 - ty    # ID가 이력서에 해당하면 모집글로, 모집글이면 이력서로
    frame = frame[frame['종류']==t]
    frame = frame.reset_index(drop=True) # index 리셋
    frame = has_skill(desc1, frame, t) # 기술스택이 있는 이력서 데이터만 뽑음
    print(len(frame))
    
    embedding = model.encode(wr)
    frame['score'] = frame.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    ans = frame.sort_values(by='score', ascending=False).head(30).reset_index(drop=True)
    print(ans)
    ans_list = []
    for i in range(30):
        try:
            ans_list.append(ans.loc[i,'ID'])
        except:
            break
    return ans_list

    # # 텍스트 전처리
    # wr = sub_exc(wr)
    
    # # 데이터에 추가
    # name.append(na)
    # writing.append(wr)
    # types.append(ty)
    
    # # Tf-idf
    # tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=10000,
    #                              min_df=0, # stop_words='english',
    #                              use_idf=True, tokenizer=tokenize_only)
    
    # tfidf_matrix = tfidf_vectorizer.fit_transform(list(writing)) # 글을 vectorize하기
    
    # dist = 1 - cosine_similarity(tfidf_matrix)

    # # MDS
    # MDS()
    # mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    # pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
    # xs, ys = pos[:, 0], pos[:, 1]
    # MDSdf = pd.DataFrame(dict(x=xs, y=ys, label=types, ID=name))
    # ID = na # 이력서/모집글을 합한 df에서의 primary key값
    # IDidx = len(MDSdf)-1
    # ID_dot = tuple([MDSdf.loc[IDidx]['x'], MDSdf.loc[IDidx]['y']])

    
    # # 모든 이력서에 대한 점 튜플 생성
    # dots = []
    # for i in range(len(df)):
    #     dot = tuple([df.iloc[i][0], df.iloc[i][1]])
    #     dots.append(dot)
    
    # distances = []
    # for i in range(len(dots)):
    #     distances.append(distance.euclidean(ID_dot, dots[i]))
    
    # sortedDist = sorted(distances)
    # min0 = distances.index(sortedDist[0])
    # min1 = distances.index(sortedDist[1])
    # min2 = distances.index(sortedDist[2])
    # min3 = distances.index(sortedDist[3])
    # min4 = distances.index(sortedDist[4])

    # print('top 5 매칭 결과 : ')
    # print('1. ' + df.iloc[min0]['ID'])
    # print('2. ' + df.iloc[min1]['ID'])
    # print('3. ' + df.iloc[min2]['ID'])
    # print('4. ' + df.iloc[min3]['ID'])
    # print('5. ' + df.iloc[min4]['ID'])
    
    # return df.iloc[min0]['ID'], df.iloc[min1]['ID'], df.iloc[min2]['ID'], df.iloc[min3]['ID'], df.iloc[min4]['ID']



########## (이력서 관련)파일에서 텍스트 읽어오기(pdf, docx, hwp) ###########
def get_pdf_text(filename):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = "utf-8"
    laparams = LAParams()
    device = TextConverter(
        rsrcmgr, 
        retstr, 
        codec=codec, 
        laparams=laparams
    )
    fp = open(filename, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    pages = PDFPage.get_pages(
        fp, 
        pagenos, 
        maxpages=maxpages, 
        password=password, 
        caching=caching, 
        check_extractable=True
    )
    for page in pages:
        interpreter.process_page(page)

    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text

try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile

NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PARA = NAMESPACE + 'p'
TEXT = NAMESPACE + 't'

def get_docx_text(filename):
    document = zipfile.ZipFile(filename)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)
    paragraphs = []
    for paragraph in tree.getiterator(PARA):
        texts = [node.text
                for node in paragraph.getiterator(TEXT)
                if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    return '\n\n'.join(paragraphs)

def get_hwp_text(filename):
    f = olefile.OleFileIO(filename)
    dirs = f.listdir()

    # 문서 포맷 압축 여부 확인
    header = f.openstream("FileHeader")
    header_data = header.read()
    is_compressed = (header_data[36] & 1) == 1

    # Body Sections 불러오기
    nums = []
    for d in dirs:
        if d[0] == "BodyText":
            nums.append(int(d[1][len("Section"):]))
    sections = ["BodyText/Section"+str(x) for x in sorted(nums)]

    # 전체 text 추출
    text = ""
    for section in sections:
        bodytext = f.openstream(section)
        data = bodytext.read()
        if is_compressed:
            unpacked_data = zlib.decompress(data, -15)
        else:
            unpacked_data = data
    
        # 각 Section 내 text 추출    
        section_text = ""
        i = 0
        size = len(unpacked_data)
        while i < size:
            header = struct.unpack_from("<I", unpacked_data, i)[0]
            rec_type = header & 0x3ff
            rec_len = (header >> 20) & 0xfff

            if rec_type in [67]:
                rec_data = unpacked_data[i+4:i+4+rec_len]
                section_text += rec_data.decode('utf-16')
                section_text += "\n"

            i += 4 + rec_len

        text += section_text
        text += "\n"

    return text
