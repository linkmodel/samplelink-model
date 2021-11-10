#!/usr/bin/env python

from setuptools import setup, find_packages

with open("requirements.txt", "r") as FH:
    REQUIREMENTS = FH.readlines()

NAME = 'samplelink-model'
VERSION = '0.0.1'
DESCRIPTION = 'Samplelink Model: A high level datamodel of computer systems ontology entities and associations'
URL = 'https://github.com/linkmodel/samplelink-model'
AUTHOR = 'Noel McLoughlin'
EMAIL = 'noel.mcloughlin@gmail.com'
REQUIRES_PYTHON = '>=3.7'
LICENSE = 'BSD'

setup(
    name=NAME,
    author=AUTHOR,
    version=VERSION,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license=LICENSE,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[r for r in REQUIREMENTS if not r.startswith("#")],
    keywords='Samplelink-Model Samplelink LinkML Datamodel',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Computer Industry',
        'Topic :: Scientific/Engineering :: Compute-Informatics',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
