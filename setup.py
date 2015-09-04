#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

classifiers = ["Development Status :: Beta",
               "Intended Audience :: Developers",
               "Operating System :: OS Independent",
               "Programming Language :: Python :: 2.7",
               "Operating System :: OS Independent",
               'Topic :: Software Development :: Libraries :: Python Modules',
]

long_description = open('README.md').read()

setup(name='youtube-api',
      version='1.0',
      description="""
      A basic Python wrapper for the Youtube Data API v3 ( Non-OAuth ).
      Designed to let devs easily fetch public data (Video, Channel, Playlists
      info) from Youtube.""",
      long_description=long_description,
      classifiers=classifiers,
      keywords='client to youtube api v3',
      author='Ronen Hayun',
      packages=find_packages(exclude=('doc', 'docs',)),
      include_package_data=True,
)
