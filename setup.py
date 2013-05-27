try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'authur': 'Erik Wong',
    'url': 'http://github.com/k4orta/abathur',
    'author_email': 'ewong@blizzard.com',
    'version': '0.1',
    'install_requires': ['sc2reader', 'pyyaml'],
    'packages': ['abathur'],
    'scrips': [],
    'name': 'Abathur Replay Parser'
}

setup(**config)
