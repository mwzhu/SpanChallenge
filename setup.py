from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name = 'JSON Converter',
    version = '1.0',
    description = 'A module to convert JSON files containing notifications from an old format to a new format which also removes duplicates and sorts notifications',
    license = 'MIT',
    long_description = long_description,
    author = 'Michael Zhu',
    author_email = 'michaelwzhu@berkeley.edu',
    packages = ['JSON Converter'],
    install_requires = ['dateutil']
)
