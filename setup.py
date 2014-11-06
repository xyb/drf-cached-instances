#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging setup for drf-cached-instances."""

from drf_cached_instances import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Django>=1.6',
    'pytz',
    'djangorestframework',
]

test_requirements = [
    'dj_database_url',
    'django_nose',
    'django_extensions',
    'mock',
]

setup(
    name='drf-cached-instances',
    version=version,
    description='Cached instances for Django REST Framework',
    long_description=readme + '\n\n' + history,
    author='John Whitlock',
    author_email='john@factorialfive.com',
    url='https://github.com/jwhitlock/drf-cached-instances',
    packages=[
        'drf_cached_instances',
    ],
    package_dir={
        'drf_cached_instances': 'drf_cached_instances',
    },
    include_package_data=True,
    install_requires=requirements,
    license="MPL 2.0",
    zip_safe=False,
    keywords='drf-cached-instances',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='sample_site.runtests.runtests',
    tests_require=test_requirements
)
