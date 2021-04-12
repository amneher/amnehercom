#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='amneher',
    version='1.0',
    description='My Blog',
    author='Andrew Neher',
    author_email='andrew.neher1@gmail.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},  # Root modules.
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'manage=amneher.manage:main',
        ],
    },
)
