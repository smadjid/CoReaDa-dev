try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CoReaDa',
    'author': 'Madjdi SADALLAH',
    'url': '...',
    'download_url': '...',
    'author_email': 'msadallah@cerist.dz',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CoReaDa'],
    'scripts': [],
    'name': 'coreada'
}

setup(**config)
