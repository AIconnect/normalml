#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup
from setuptools import setup, find_packages
setup(name='normalml',
            version='1.0',
            py_modules=['normalml'],
            packages=find_packages(),

      install_requires = ['numpy','scipy','matplotlib'],
      author = "Li QiuRui",
      author_email = "1012695904@qq.com",
      description = "This is an normal ml Package",
      license = "PSF",
      keywords = "hello world ! machine learning!",
      url = "https://github.com/aiconnect",   # project home page, if any

            )


