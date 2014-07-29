# coding=utf8
import os
import re
import csv
import codecs
import pkg_resources


def slug(s):
    # naivest possible slugger
    s = re.sub('[^A-z\- ]', '', s)
    return s.replace(' ', '-').lower()


def static_url(fullpath):
    return "static/images/work/{}".format(os.path.basename(fullpath))


class Work(object):

    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    @property
    def image(self):
        static_dir = pkg_resources.resource_filename('lostproperty', 'static')
        target = os.path.join(static_dir, 'images', 'work', slug(self.title) + '.jpg')
        placeholder = "static/images/portfolioplaceholder.gif"
        path = target if os.path.exists(target) else placeholder
        return static_url(path)


def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def populate_examples():
    csv_file = os.path.join(os.path.dirname(__file__), 'work.csv')
    with codecs.open(csv_file, encoding='utf8') as fo:
        reader = unicode_csv_reader(fo)
        for row in reader:
            title, url, desc = row
            yield Work(title, url, desc)


examples = list(populate_examples())
