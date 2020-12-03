import requests
import json

url = 'https://kauth.kakao.com/oauth/token'

REST_API_KEY = "6e325c391dbe37d00ce5f3ffd0e97525"
REFRESH_TOKEN = "F91lzr6pu8xWVSPohQ6E7cQAPBFtVA6pAXMJeAo9c00AAAF0zn1uWA",

data = {
    "grant_type" : "refresh_token",
    "client_id" : REST_API_KEY,
    "refresh_token" : REFRESH_TOKEN
}

response = requests.post(url, data=data)
tokens = response.json()

print(response.status_code)
print(tokens)

with open("currentAccessToken.json", "w") as fp :
    json.dump(tokens, fp)

# 생성된 토큰 가져오기
with open("currentAccessToken.json", "r") as f :
    ts = json.load(f)
    
    print(ts['access_token'])
    print("success")

