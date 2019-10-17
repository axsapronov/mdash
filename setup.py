#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "six",
]

setup(
    version='3.5',
    author="Evgeny Muravjev & Alexander Drutsa",
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    description="Evgeny Muravjev Typograph",
    long_description=readme,
    include_package_data=True,
    keywords='mdash',
    name='mdash',
    packages=[
        'EMT',
    ],
    package_dir={
        'EMT': 'src-py'
    },
    url='https://github.com/emuravjev/mdash',
    zip_safe=False,
)
