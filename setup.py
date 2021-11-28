#!/usr/bin/env python

from distutils.core import setup
from django_sidecar import __version__

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django_sidecar',
    version=__version__,
    description='django sidecar pattern implementation',
    author='svtter',
    author_email='svtter@163.com',
    url='',
    packages=['django_sidecar'],
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown')
