#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='{{ rubick.repo_name }}',
    version='{{ rubick.version }}',
    description='{{ rubick.project_short_description }}',
    long_description=readme + '\n\n' + history,
    author='{{ rubick.full_name }}',
    author_email='{{ rubick.email }}',
    url='https://github.com/{{ rubick.github_username }}/{{ rubick.repo_name }}',
    packages=[
        '{{ rubick.repo_name }}',
    ],
    package_dir={'{{ rubick.repo_name }}':
                 '{{ rubick.repo_name }}'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='{{ rubick.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
