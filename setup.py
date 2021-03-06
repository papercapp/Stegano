#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'stegano',
    'stegano.exif'
]

requires = ['pillow']

with open('README.rst', 'r') as f:
    readme = f.read()
with open('CHANGELOG.rst', 'r') as f:
    changelog = f.read()

setup(
    name='Stegano',
    version='0.5.1',
    author='Cédric Bonhomme',
    author_email='cedric@cedricbonhomme.org',
    packages=packages,
    include_package_data=True,
    scripts=['bin/slsb', 'bin/slsb-set', 'bin/steganalysis-parity'],
    url='https://github.com/cedricbonhomme/Stegano',
    description='A Python Steganography module.',
    long_description=readme + '\n\n' + changelog,
    platforms = ['Linux'],
    license='GPLv3',
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)
