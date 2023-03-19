import requests
import json
resp=requests.post("https://reqres.in/api/users",data=json.loads(open("data.json","r").read()))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()["job"]=="ML Engineer"