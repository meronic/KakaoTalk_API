import requests
import json

ACCESS_TOKEN = ''
# 생성된 토큰 가져오기
with open("currentAccessToken.json", "r") as f :
    ts = json.load(f)
    
    ACCESS_TOKEN = str(ts['access_token'])



url = "https://kapi.kakao.com/v1/api/talk/friends?limit=3/"
data = {
    "Authorization": "Bearer " + ACCESS_TOKEN
}

response = requests.get(url, data=data)
print(response.status_code)




