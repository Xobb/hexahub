#!/usr/bin/env python
import hexahub
from setuptools import setup, find_packages

setup(
    name='hexahub',
    version=hexahub.__version__,
    description='Low level Python and CLI interface to GitHub',
    long_description=open('README.rst').read(),
    author='Alon Swartz',
    author_email='alon@turnkeylinux.org',
    url='https://github.com/Xobb/hexahub',
    packages=find_packages(),
    package_dir={'hexahub': 'hexahub'},
    zip_safe=True,
    install_requires=[
        'simplejson',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'hexahub=hexahub.cmd:main'
        ]
    }
)
