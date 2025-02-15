
import datetime
import requests
from requests_html import HTML
import pandas as pd

now = datetime.datetime.now()
year = now.year

def url_to_txt(url, filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_txt = r.text
        if save:
            with open(f"world-{year}.html", 'w', encoding="utf-8") as f:
                f.write(html_txt)
        return html_txt



url ="https://www.boxofficemojo.com/year/world/"

html_text = url_to_txt(url)

r_html = HTML(html=html_text)

# print(r_html.find("table"))

table_class = ".imdb-scroll-table"  # with class selector
table_class = "#table"  # with id selector
r_table = r_html.find(table_class)
# print(r_table)
# print(len(r_table))
# print(type(r_table))
# print(r_table[0])    # given output :  <Element 'div' id='table' class=('a-section', 'imdb-scroll-table', 'mojo-gutter')>
# print(r_table[0].text)
# print(r_table[0])
table_data = []
header_names=[]
if len(r_table) == 1:
    # print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    # print(header_row)
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    table_data = []
    # print(header.text)
    for row in rows[1:]:
        # print(row.text)
        cols = row.find("td")
        row_data = []
        for i,col in enumerate(cols):
            # print(i, col.text, '\n\n')
            row_data.append(col.text)
        table_data.append(row_data)
    # print(rows)

# print(header_names)
# # print(table_data)
# print(table_data[0])


df = pd.DataFrame(table_data, columns= header_names)
df.to_csv('files.csv', index=False)

