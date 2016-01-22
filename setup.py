# coding: utf-8

import re

from os.path import dirname, join, abspath
from setuptools import setup

VERSION = re.search(
    r"__version__\s=\s'(\d\.\d\.\d)'",
    open(abspath(join(dirname(__file__), 'marcel.py'))).read()
    ).group(1)

setup(
    name="marcel",
    version=VERSION,
    license='3-clause BSD',
    description='Le docker français',
    author="Balthazar Rouberol",
    author_email="br@imap.cc",
    url='http://github.com/brouberol/marcel',
    py_modules=['marcel'],
    entry_points={'console_scripts': ['marcel=marcel:main']},
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Build Tools',
        ]
    )
