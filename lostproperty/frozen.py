from flask_frozen import Freezer
from application import app
import settings

freezer = Freezer(app)


@freezer.register_generator
def work_details():
    for key in settings.PROJECTS.keys():
        yield {'id': key}

if __name__ == '__main__':
    freezer.freeze()
