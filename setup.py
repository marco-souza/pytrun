#! /usr/bin/env python3
"""(pytrun) Python Yaml Task RUNner."""
from setuptools import setup, find_packages
from os import path, getenv

project_path = path.abspath(path.dirname(__file__))

# load full description
with open(path.join(project_path, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    # Package Info
    name='pytrun',
    version=getenv('pkg_version', None),
    description="Python Yaml Task RUNner.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='https://github.com/marco-souza/pythun',
    author='Marco Antônio',
    author_email='ma.souza.junior@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Meta data
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developer',
        'Topic :: Tool :: Task Runner',

        'Programming Language :: Python :: 3.6'
    ],
    keywords='python yaml task runner',
    entry_points={
        # Add console_scripts
        'console_scripts': [
            'pytrun = pytrun.main:main'
        ],
    },

    # Dependencies
    install_requires=[
        'pyyaml',
    ],
    extras_require={
        'dev': [
            'rope',
            'flake8',
            'pylint',
            'pycodestyle',
        ],
        'test': [],
    },
)