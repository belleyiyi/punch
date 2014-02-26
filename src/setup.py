'''
Created on Feb 20, 2014

@author: luqin
'''
from setuptools import setup

setup(
    name='punch',
    version='1.0',
    long_description=__doc__,
    packages=['punch'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)