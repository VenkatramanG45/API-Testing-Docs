import requests
import json

#my_data=open("data.json","r").read()
my_data={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
#resp=requests.post("https://reqres.in/api/users",data=json.loads(my_data))
#resp=requests.post("https://reqres.in/api/users",data=my_data) The end point should be changed
resp=requests.post("https://reqres.in/api/register",data=my_data)
print(resp)
#print(resp.json())
print(resp.json()["token"])
#assert resp.json()["job"]=="ML Engineer"