import requests
import json
import time
import datetime

# https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=6e325c391dbe37d00ce5f3ffd0e97525&redirect_uri=https://localhost.com
# REST_Key = "6e325c391dbe37d00ce5f3ffd0e97525"
# code = "5_o4NAKT8oO51BCJT6J0YqiEcdCVCIxDf7dxLzYNHDMjWlh5XX001q6qwiqapAFRh5YyigorDR4AAAF0znuc0g"

# url = "https://kauth.kakao.com/oauth/token"
# # url = 'http://localhost.com/'



# data = {
#     "grant_type" : "authorization_code",
#     "client_id" : REST_Key,
#     "redirect_uri" : "https://localhost.com",
#     "code" : code
# }


url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "UCWyQv00PqEwF-IaZsO73SXRwCaL4ScBVCByyQo9c00AAAF0zn1uWA"
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


for i in range(10) : 
    now = datetime.datetime.now()
    send_kakao(str(now))
    time.sleep(0.5)
    

# response = requests.post(url, data=data)
# tokens = response.json()

# print(response.status_code)
# print(tokens)

# with open("kakao_code.json", "w") as fp:
#     json.dump(tokens, fp)

