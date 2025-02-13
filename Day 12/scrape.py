import requests

url ="https://www.boxofficemojo.com/year/world/"

r = requests.get(url)
print(r)
print(r.status_code)