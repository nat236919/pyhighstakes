"""
FILE: setup.py
DESCRIPTION: Set up PyPI as a Python Library
DATE: 27-Jan-2020
"""

import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author='Nuttaphat Arunoprayoch',
    author_email='nat236919@gmail.com',
    name='pyhighstakes',
    license='MIT',
    description='PyHighStakes is a library offering card decks and games',
    version='v0.0.1',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/nat236919/pyhighstakes',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop'
    ],
)