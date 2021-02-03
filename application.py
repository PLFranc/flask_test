from flask import Flask, render_template
application = Flask(__name__)
app = application


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/pronoo')
def pronoo():
    return render_template('pronoo.html')


if __name__ == '__main__':
    application.run(debug=True)
