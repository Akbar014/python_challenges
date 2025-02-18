
import requests

ngrok_url ="https://6dfe-103-96-104-33.ngrok-free.app"
endpoint = f"{ngrok_url}/box-office-mojo-scrapper"

r = requests.post(endpoint, json={})
print(r.text)
# print(r.json()['data'])
