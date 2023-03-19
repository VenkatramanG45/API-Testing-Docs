import requests
resp=requests.delete("https://reqres.in/api/users/2")
#print(resp.json())
print(resp.status_code)
assert resp.status_code==204,"User Deletion Failed"

