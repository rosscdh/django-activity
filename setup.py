# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name = "django-activity",
    version = "0.0.1",
    author = "Ross Crawford-d'Heureuse",
    author_email = "sendrossemail+django-activity@gmail.com",
    description = ("Django app providing an extensible simple activity log"),
    license = "MIT",
    keywords = "django activity stream log",
    url = "https://github.com/rosscdh/django-activiy",
    packages=['django-jsonfield'],
    install_requires = [
        'django-jsonfield',
    ]
)