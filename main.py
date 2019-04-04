from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/siteInformation')
def siteInformation():
    return render_template('siteInformation.html')


if __name__ == '__main__':
    app.run(debug=True)

