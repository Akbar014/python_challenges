

from flask import Flask
from lxml_html_clean import Cleaner
from scrape import run as scrape_runner

app = Flask(__name__)


@app.route("/", methods=['GET'] )
def hello_world():
    return "Hello world. This is Flask from server1.py"


@app.route("/abc", methods=['GET'] )
def abc_world():
    return "Hello world. This is from another route /abc"



@app.route("/box-office-mojo-scrapper", methods=['GET'])
def box_office_scraper_view():
    scrape_runner()
    return "Done"



# if __name__ == '__main__':
#     app.run(debug=True, port=8000)