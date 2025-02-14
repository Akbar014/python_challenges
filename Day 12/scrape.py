import datetime
import requests


now = datetime.datetime.now()
year = now.yea




def url_to_file(url, filename='world.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_txt = r.text
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(html_txt)
        return html_txt

url ="https://www.boxofficemojo.com/year/world/"
url_to_file(url)

# r = requests.get(url)
# print(r.text)
# print(r.status_code)