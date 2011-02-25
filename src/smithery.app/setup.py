# Smithery
# 
# Copyright (c) 2011 B-Open Solutions srl. All rights reserved.
# Copyright (c) 2010-2011 Alessandro Amici. All rights reserved.
#
# Distributed under the terms of the ZPL 2.1

from setuptools import setup, find_packages

version = '0.4'
tests_require=['zope.testing', 'zc.buildout']

setup(
    name='smithery.app',
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
    url='http://github.com/alexamici/smithery',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['smithery'], 
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'zc.buildout>=1.4.0',
        'smithery.recipe.miners',
        'smithery.recipe.smiths',
    ],
    entry_points={
        'console_scripts': [
            'smithery = smithery.app:main',
        ],
    }, 
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
)
