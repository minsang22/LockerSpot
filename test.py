import requests
import json

server_addr = "http://10.223.113.129:8000"
data = {"name" : "코리안섹스머신성정규", "student_id" : "201911113213121", "password" : "12",  "path": "/student/signin"}
res = requests.post(server_addr, json = data, headers={"accept": "application/json","Content-Type": "application/json",})

print(res.json()["status"])