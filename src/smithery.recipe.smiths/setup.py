# -*- coding: utf-8 -*-
"""
This module contains the tool of smithery.recipe.smiths
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
        'default = smithery.recipe.smiths:Cheetah', 
        'cheetah = smithery.recipe.smiths:Cheetah', 
        'chameleon = smithery.recipe.smiths:Chameleon', 
        'xpath = smithery.recipe.smiths:XPath', 
    ], 
}
tests_require=['zope.testing', 'zc.buildout']

setup(
    name='smithery.recipe.smiths',
    version=version,
    description="A collection of recipes to publish metadata",
    long_description=long_description,
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
    install_requires=[
        'setuptools',
        'zc.buildout',
        'Cheetah',
        'Chameleon',
    ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite = 'smithery.recipe.smiths.tests.test_docs.test_suite',
    entry_points=entry_points,
)
