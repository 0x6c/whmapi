#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='whmapi',
    version='0.0.1a',
    description='WHMApi pytthon module',
    long_description=readme,
    author='Andrey Storchak',
    author_email='andrey.storchak@gmail.com',
    url='https://github.com/0x6c/whmapi.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
