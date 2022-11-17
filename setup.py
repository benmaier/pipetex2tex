from setuptools import setup, Extension
import setuptools
import os
import sys

# get __version__, __author__, and __email__
exec(open("./pipetex2tex/metadata.py").read())

setup(
    name='pipetex2tex',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/benmaier/pipetex2tex',
    license=__license__,
    description="A short description of the package.",
    long_description='',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
                'numpy>=1.17',
    ],
    tests_require=['pytest', 'pytest-cov'],
    setup_requires=['pytest-runner'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 ],
    project_urls={
        'Documentation': 'http://pipetex2tex.benmaier.org',
        'Contributing Statement': 'https://github.com/benmaier/pipetex2tex/blob/master/CONTRIBUTING.md',
        'Bug Reports': 'https://github.com/benmaier/pipetex2tex/issues',
        'Source': 'https://github.com/benmaier/pipetex2tex/',
        'PyPI': 'https://pypi.org/project/pipetex2tex/',
    },
    include_package_data=True,
    zip_safe=False,
)
