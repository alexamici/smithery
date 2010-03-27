# -*- coding: utf-8 -*-
"""
This module contains the tool of smithery.recipe.smiths
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('smithery', 'recipe', 'smiths', 'README.txt')
    + '\n' +
    'Contributors\n' 
    '************\n'
    + '\n' +
   'Download\n'
    '********\n'
    )
entry_point = 'smithery.recipe.smiths:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require=['zope.testing', 'zc.buildout']

setup(name='smithery.recipe.smiths',
      version=version,
      description="A collection of recipes to publish metadata",
      long_description=long_description,
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Zope Public License',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['smithery', 'smithery.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'smithery.recipe.smiths.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
