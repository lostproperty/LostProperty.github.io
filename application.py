from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index(name=None):
        return render_template('index.html', home=True)

@app.route('/services.html')
def services(name=None):
        return render_template('services.html')

@app.route('/team.html')
def team(name=None):
        return render_template('team.html')

@app.route('/contact.html')
def contact(name=None):
        return render_template('contact.html')

@app.route('/technology.html')
def technology(name=None):
        return render_template('technology.html')

@app.route('/work.html')
def work(name=None):
        return render_template('work.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
