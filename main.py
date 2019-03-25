from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/test')
def test():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s.</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h2>Greeting %s!</h2>' % name


if __name__ == '__main__':
    app.run(debug=True)

