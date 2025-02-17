

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'] )
def hello_world():
    return "Hello world. This is Flask from server1.py"


@app.route("/abc", methods=['GET'] )
def abc_world():
    return "Hello world. This is from another route /abc"



# if __name__ == '__main__':
#     app.run(debug=True, port=8000)