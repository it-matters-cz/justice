#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['dateparser>=1.1.8,<2', 'pyquery>=1.4.3,<2']

setup_requirements = []

test_requirements = ['flake8']

setup(
    author="Jakub Boukal",
    author_email='www.bagr@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="A python package to download company information from https://justice.cz/",
    entry_points={
        'console_scripts': [
            'justice=justice.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='justice',
    name='justice',
    packages=find_packages(include=['justice', 'justice.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SukiCZ/justice',
    version='0.1.8',
    zip_safe=False,
)
