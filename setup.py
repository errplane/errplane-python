import os
from setuptools import setup, find_packages

setup(
    name='errplane',
    version='0.1.6',
    author='Todd Persen',
    author_email='todd@errplane.com',
    packages=find_packages(),
    url='http://github.com/errplane/errplane-python',
    license='LICENSE.txt',
    description='Python library for use with Errplane (https://errplane.com)',
    install_requires=[
      "requests"
    ],
)
