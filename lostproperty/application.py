from flask import Flask
from flask import render_template
import settings
app = Flask(__name__)
app.config.from_object(settings)
from datetime import datetime
from functools import wraps


def no_sitemap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.no_sitemap = True
    return wrapper


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/robots.txt')
@no_sitemap
def robots():
    return render_template('robots.txt')


@app.route('/404.html')
@no_sitemap
def error_404(name=None):
    return render_template('404.html')


@app.route('/CNAME')
def cname():
    return render_template('CNAME')


@app.route('/work.html')
def work():
    return render_template('work.html')


@app.route('/work/<id>.html')
def work_details(id):
    return render_template('projects/%s.html' % id, id=id, **settings.PROJECTS[id])


@app.route('/sitemap.xml', methods=['GET'])
@no_sitemap
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages = []
    now = datetime.now().isoformat()
    # static pages
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods \
            and not hasattr(app.view_functions[rule.endpoint], 'no_sitemap') \
                and len(rule.arguments) == 0:
            pages.append([rule.rule, now])

    sitemap_xml = render_template('sitemap.xml', pages=pages)
    response = app.make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
