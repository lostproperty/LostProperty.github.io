from collections import OrderedDict

TITLE = 'Lost Property'
TAGLINE = "We bring our clients' digital products and services to life"
SHORT_DESCRIPTION = 'Lost Property is a product agency with a passion for creating products that people actually want to use.'

DESCRIPTION = 'Lost Property is a product agency with a passion for creating products that people actually want to use.'

KEYWORDS = 'python, javascript, product, technology, utility, lost property, international, craft, web, digital'

LOGOS = [
    ('amvbbdo.png', '/work/graduate.html'),
    ('sainsburys.png', '/work/foodrescue.html'),
    ('handcircus.png', '/work/seabeard.html'),
    ('catinaflat.png', '/work/catinaflat.html'),
    ('google.png', '/work/foodrescue.html'),
    ('unilever.png', '/work/allthingshair.html'),
    ('razorfish.png', '/work/allthingshair.html'),
    ('qmul.png', '/work/warblr.html'),
    ('breel.png', '/work/foodrescue.html'),
]

NAVBAR = OrderedDict(
    [
        ('Our Work', '/work.html'),
   #     ('About', '/about.html'),
   #     ('Blog', 'http://blog.lostpropertyhq.com/'),
        ('Twitter', 'http://twitter.com/lostpropertyhq'),
    #    ('Contact', '/contact.html'),
    ]
)

TWITTER = 'lostpropertyhq'
EMAIL = 'hello@lostpropertyhq.com'
PHONENUMBER = '+44 20 3111 0112'
ADDRESS = [
    'Lost Property',
    'Studio 13',
    'The Trampery',
    '125-127 Mare Street',
    'E8 3RH'
]

PROJECTS = {
    'catinaflat': {
        'title': 'Cat in a Flat',
        'tagline': "London's Trusted Cat Sitting Community",
        'link': "https://catinaflat.com",
    },
    'graduate': {
        'title': 'AMV BBDO Graduate',
        'client': 'AMV BBDO',
        'tagline': "UK's most creative graduate scheme",
        'link': "https://graduates.amvbbdo.co.uk",
    },
    'allthingshair': {
        'title': 'All Things hair',
        'client': 'Unilever',
        'agency': 'Razorfish',
        'tagline': "For more hair inspiration and tips",
        'link': "https://allthingshair.com",
        'award': "BIMA, Webby, Brand Republic",
    },
    'hairid': {
        'title': 'Hair ID',
        'client': 'Unilever',
        'agency': 'Razorfish',
    },
    'theyuseit': {
        'title': "TheyUse.It",
        'tagline': "Make your company known and find talent",
        'link': "https://theyuse.it",
    },
    'nexxus': {
        'title': 'NEXXUS',
        'client': 'Unilever',
        'agency': 'Razorfish',
    },
    'seabeard': {
        'title': 'Seabeard',
        'client': 'Handcircus',
        'tagline': "A world of adventure in your pocket!",
        'link': "https://itunes.apple.com/us/app/seabeard/id913754563",
        'award': "Editor's choice",
    },
    'warblr': {
        'title': 'Warblr',
        'client': "Queen Mary London University",
        'link': "https://www.kickstarter.com/projects/1190241008/warblr-an-app-that-recognises-birds-from-their-son"
    },
    'foodrescue': {
        'title': "Sainsbury's Food Rescue",
        'client': "Sainsbury's, Google",
        'agency': "b-reel",
        'tagline': "A platform to end food waste",
        'link': "http://www.sainsburysfoodrescue.co.uk/",
        'award': "FWA",
    },

}
