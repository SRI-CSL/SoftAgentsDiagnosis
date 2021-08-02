# from distutils.core import setup
from setuptools import setup, find_packages
import os
import glob

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# use the in house version number so we stay in synch with ourselves.
from deviation.version import deviation_version

setup(
    name='Deviation',
    version=deviation_version,
    description='The SoftAgent Deviation Tool',
    long_description=long_description,
    url='https://github.com/SRI-CSL/SoftAgents/Deviation',
    author='Ian A. Mason',
    author_email='iam@csl.sri.com',


    packages=find_packages(exclude=['tests']),

    entry_points = {
        'console_scripts': [
            'deviate = deviation.main:main',
        ],
    },



    license='MIT',

    install_requires=[
        "antlr4-python3-runtime >= 4.9",
        "yices >= 1.1.0"
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Topic :: System :: Distributed Computing',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
