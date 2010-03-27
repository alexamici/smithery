# Smithery
# 
# Copyright (c) 2010 by Alessandro Amici. All rights reserved.
#
# Distributed under the terms of the ZPL 2.1


from setuptools import setup, find_packages
import sys, os

version = '0.1'

tests_require=['zope.testing', 'zc.buildout']

setup(
    name='smithery',
    version=version,
    description="Collect and reformat data",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    keywords='',
    author='Alessandro Amici',
    author_email='a.amici@bopen.it',
    url='http://github.com/alexamici/Smithery',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zc.buildout>=1.4.0',
        'Cheetah',
    ],
    entry_points={
        'console_scripts': [
            'smithery = smithery.app:main',
        ],
        'zc.buildout': [
            'default = smithery.recipe:Worker'
        ],
    }, 
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
)
