# -*- coding: utf-8 -*-
"""
This module contains the tool of smithery.recipe.miners
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.3'

long_description = (
    read('README')
)

entry_points = {
    'zc.buildout': [
        'default = smithery.recipe.miners:Namespace', 
        'namespace = smithery.recipe.miners:Namespace', 
        'file = smithery.recipe.miners:File', 
        'folder = smithery.recipe.miners:Folder', 
        'csv = smithery.recipe.miners:Csv', 
        'wms = smithery.recipe.miners:WMS', 
        'google_calendar = smithery.recipe.miners:GoogleCalendar', 
    ], 
}

tests_require=['zope.testing', 'zc.buildout']

setup(
    name='smithery.recipe.miners',
    version=version,
    description="A collection of base recipes for metadata extranction",
    long_description=long_description,
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Zope Public License',
    ],
    keywords='',
    author='Alessandro Amici',
    author_email='alexamici@gmail.com',
    url='http://github.com/alexamici/smithery',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['smithery', 'smithery.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
        'zc.buildout',
        'OWSLib',
    ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite = 'smithery.recipe.miners.tests.test_docs.test_suite',
    entry_points=entry_points,
)
