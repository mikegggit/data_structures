#!/usr/bin/python

from setuptools import setup, find_packages, find_namespace_packages
setup(
    name="datastructures-mikeggg",
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description="python implementations of various data structures"
)
