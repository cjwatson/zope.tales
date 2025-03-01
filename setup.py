##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.tales package
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


TESTS_REQUIRE = [
    'zope.testing',
    'zope.testrunner',
]


setup(
    name='zope.tales',
    version='5.2.0.dev0',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description='Zope Template Application Language Expression Syntax '
                '(TALES)',
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
    ),
    keywords="zope template xml tales",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 4',
        'Framework :: Zope :: 5',
    ],
    url='https://github.com/zopefoundation/zope.tales',
    project_urls={
        'Documentation': 'https://zopetales.readthedocs.io/',
        'Issue Tracker': 'https://github.com/zopefoundation/zope.tales/issues',
        'Sources': 'https://github.com/zopefoundation/zope.tales',
    },
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
    extras_require={
        'test': TESTS_REQUIRE,
        'tal': [
            'zope.tal',
        ],
        'docs': [
            'Sphinx',
            'repoze.sphinx.autointerface',
            'zope.tal',
        ],
    },
    install_requires=[
        'setuptools',
        'zope.interface',
        'six',
    ],
    tests_require=TESTS_REQUIRE,
    include_package_data=True,
    zip_safe=False,
)
