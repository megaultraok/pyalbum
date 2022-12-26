#!/usr/bin/env python

from setuptools import setup, find_packages
import io
import os

NAME = 'Pyalbum'
VERSION = '1.0'
DESCRIPTION = 'Your favorite album, generated by Python with the help of Wikipedia!'
AUTHOR = 'Jada White'
EMAIL = 'jadawhite@megaultraok.dev'
REQUIRED = [
    'anyio==3.5.0',
    'beautifulsoup4==4.11.1',
    'bs4==0.0.1',
    'certifi==2021.10.8',
    'charset-normalizer==2.0.12',
    'h11==0.12.0',
    'httpcore==0.14.7',
    'httpx==0.22.0',
    'idna==3.3',
    'requests==2.27.1',
    'rfc3986==1.5.0',
    'sniffio==1.2.0',
    'soupsieve==2.3.2.post1',
    'urllib3==1.26.9',
    'wikipedia==1.4.0',
    'youtube-dl==2021.12.17',
   ' youtube-search-python==1.6.5'
]

# README as long description
try:
    with io.open(os.path.join('.', 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    license='MIT'
)