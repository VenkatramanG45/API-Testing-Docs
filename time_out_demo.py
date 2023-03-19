import requests
r=requests.get( "https://httpbin.org/delay/5",timeout=3)
print(r.status_code)