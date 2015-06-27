pylint-werkzeug
===============

[![Build Status](https://travis-ci.org/jschaf/pylint-werkzeug.svg?branch=master)](https://travis-ci.org/jschaf/pylint-werkzeug) [![Coverage Status](https://coveralls.io/repos/jschaf/pylint-werkzeug/badge.svg)](https://coveralls.io/r/jschaf/pylint-werkzeug)

## About

`pylint-werkzeug` is [Pylint](http://pylint.org) plugin for improving code
analysis when editing code using [Werkzeug](http://werkzeug.pocoo.org/).
Inspired by [pylint-django](https://github.com/landscapeio/pylint-django).

## Usage

Ensure `pylint-werkzeug` is installed and on your path, and then run pylint.

```
pip install pylint-werkzeug
pylint --load-plugins pylint_werkzeug [..your module..]
```

## License

pylint-werkzeug is available under the GPLv2 license.