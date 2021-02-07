from flask import Flask, render_template
from get_data import get_match


application = Flask(__name__)
app = application


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/pronoo')
def pronoo():
    matchs = get_match()
    return render_template('pronoo.html', matchs = matchs)


if __name__ == '__main__':

    application.run(debug=True)
