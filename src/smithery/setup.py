# Smithery
# 
# Copyright (c) 2010 by Alessandro Amici. All rights reserved.
#
# Distributed under the terms of the ZPL 2.1


from setuptools import setup, find_packages
import sys, os

version = '0.2'

tests_require=['zope.testing', 'zc.buildout']

setup(
    name='smithery',
    version=version,
    description="Collect and reformat data",
    classifiers=[
        'Development Status :: 3 - Alpha',
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
    author_email='alexamici@gmail.com',
    url='http://github.com/alexamici/Smithery',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zc.buildout>=1.4.0',
    ],
    entry_points={
        'console_scripts': [
            'smithery = smithery.app:main',
        ],
    }, 
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
)
