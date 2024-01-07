#!/usr/bin/python3
from setuptools import setup


setup(
    name='aptly-wa',
    version='0.1',
    packages=['aptly_wa'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'aptly-wa = aptly_wa.__main__:main',
        ],
    },
    author='Darnell Otterson',
    author_email='rfolkker@gmail.com',
    description='A simple Python module for Aptly API',
    long_description=open('README.md').read(),
    url='https://github.com/rfolkker/aptly-wa.git',
)