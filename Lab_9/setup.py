#!/usr/local/bin/python
from distutils.core import setup
from distutils.extension import Extension

sincon2_ext = Extension(
    'setup',
    sources=['sincon2.cpp'],
    libraries=['boost_python'],
)

setup(
    name='sincon2-test',
    version='0.1',
    ext_modules=[sincon2_ext])
