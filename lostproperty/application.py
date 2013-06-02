from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
        return render_template('index.html', home=True)

@app.route('/services.html')
def services():
        return render_template('services.html')

@app.route('/robots.txt')
def robots():
        return render_template('robots.txt')

@app.route('/team.html')
def team():
        return render_template('team.html')

@app.route('/contact.html')
def contact():
        return render_template('contact.html')

@app.route('/technology.html')
def technology():
        return render_template('technology.html')

@app.route('/work.html')
def work(name=None):
        return render_template('work.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
