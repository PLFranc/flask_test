from flask import Flask
application = Flask(__name__)
app = application


@application.route('/')
def hello():
    return "Hello World 1"


@application.route('/index')
def index():
    return "Hey This is an index page"


if __name__ == '__main__':
    application.run(host='127.0.0.1',port=8000, debug=True)