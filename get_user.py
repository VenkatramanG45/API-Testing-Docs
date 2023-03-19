import requests
resp=requests.get("https://reqres.in/api/users?page=2")
#print(resp)
#print(type(resp))
#print(dir(resp))
code=resp.status_code
assert code==200 ,"Code doesn't match"
#print(resp.text)
#print(resp.content)
print(type(resp.headers))
print(resp.json())
print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)
