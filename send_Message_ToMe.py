import requests
import json
import time
import datetime

accessToken = ""

# 사용자 accesstoken 가져오기
with open("currentAccessToken.json", "r") as f :
    ts = json.load(f)
    accessToken = str(ts['access_token'])
    


url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + accessToken
}


def send_kakao(text) :
    
    data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : text,
                                     "link" : {
                                                 "web_url" : "www.naver.com"
                                              }
                                     
    })
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('메시지를 성공적으로 보냈습니다.')
    else:
        print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))


send_kakao("[알고리즘] 강의 [2차 과제]\n 2020-10-20 23시 59분 까지 입니다. \n 기한이 경과 되었습니다. ")
    

