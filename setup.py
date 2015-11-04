#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
  "lassie>=0.6.0",
]

setup(
  name = 'pyssb',
  version = '0.1.1',
  author = 'Leonard Lin',
  author_email = 'lhl@randomfoo.net',
  url = 'https://github.com/lhl/pyssb',
  packages = find_packages(),
  install_requires = install_requires,
  description = 'PyQT5 Site Specific Browser',
  download_url = 'https://github.com/lhl/pyssb/archive/master.zip',
  keywords = ['browser', 'ssb'],
  classifiers = [],
)
