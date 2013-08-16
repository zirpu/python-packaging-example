#!/usr/bin/env python

# example stolen from hpk42's devpi docs.
import os, sys

from setuptools import setup


if __name__ == '__main__':

    setup(
        name='example',
        description='example test project (please ignore)',
        version='1.0',
        author='Holger Krekel',
        url="http://example.com",
        author_email='holger at merlinux.eu',
        py_modules=["example"],
        zip_safe=False,

        ## i'm trying to figure out why sdist and wheel building are different for including data.
        include_package_data=True,

        # # with and without MANIFEST.in this doesn't work.
        package_data={
            'data': ['*.cfg'],
            '': ['data/*.cfg'],
        },

    )
