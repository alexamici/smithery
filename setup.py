# Smithery
# 
# Copyright (c) 2010 by Alessandro Amici. All rights reserved.
#
# Distributed under the terms of the GNU GPL v2


from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='smithery',
    version=version,
    description="Collect and reformat data",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
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
    }
)
