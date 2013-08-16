#!/usr/bin/env python

# example stolen from hpk42's devpi docs.
import os, sys

from setuptools import setup, find_packages


# setup needs to be run/found for pyroma.
#if __name__ == '__main__':

setup(
    name='example',
    description='example test project (please ignore)',
    version='1.0.1',
    author='Holger Krekel',
    url="http://example.com",
    author_email='holger at merlinux.eu',
    #py_modules=["example"],
    packages=['example'],
    zip_safe=False,

    ## i'm trying to figure out why sdist and wheel building are different for including data.
    include_package_data=True,

    # package_data isn't needed for sdist or wheel if you spec the files in MANIFEST.in 

    # this now works for building wheels, it finds the data dir in the example package
    # but does not work for sdist.
    # package_data={
    #     'example': ['data/something.cfg'],
    #     '': ['something.cfg'],
    # },

)

