import requests
import json
payload={
    "name": "API",
    #"job": "API Testing"
}
#resp=requests.put("https://reqres.in/api/users/2",data=payload)
resp=requests.patch("https://reqres.in/api/users/2",data=payload)
#resp=requests.post("https://reqres.in/api/users",data=json.loads(open("data.json","r").read()))
print(resp)
print(resp.json())
print(resp.headers.get("Content-Type"))
#assert resp.json()["job"]=="API Testing"
assert resp.json()["name"]=="API"