# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages
import sys


_version = '0.1'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-werkzeug is a Pylint plugin to aid Pylint in recognising and understanding" \
                     "errors caused when using Werkzeug"


_classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
)


_install_requires = [
    'pylint-plugin-utils>=0.2.1'
]


if sys.version_info < (2, 7):
    # pylint 1.4 dropped support for Python 2.6
    _install_requires += [
        'pylint>=1.0,<1.4',
        'astroid>=1.0,<1.3.0',
        'logilab-common>=0.60.0,<0.63',
    ]
else:
    _install_requires += [
        'pylint>=1.0',
        'astroid>=1.0',
        'logilab-common>=0.60.0',
    ]

setup(
    name='pylint-werkzeug',
    url='https://github.com/jschaf/pylint-werkzeug',
    author='Joe Schafer',
    author_email='joe@jschaf.com',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=_install_requires,
    license='GPLv2',
    classifiers=_classifiers,
    keywords='pylint werkzeug plugin'
)
