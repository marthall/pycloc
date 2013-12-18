# -*- coding: latin-1 -*-
from setuptools import setup, find_packages

setup(
    version='0.0.3',
    name='pycloc',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pycloc=src.pycloc:main'],
    },
    description='A simple tool for counting lines of code',
    author='Martin Hallén',
    author_email=['marthall@outlook.com'],
    url='http://github.com/marthall/pycloc/',
    license='MIT',
    keywords='Python count lines of code',
)
