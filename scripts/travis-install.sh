#!/bin/bash
pip install --use-mirrors coverage coveralls
pip install --use-mirrors werkzeug
pip install --use-mirrors git+https://github.com/landscapeio/pylint-plugin-utils.git@develop
pip install --use-mirrors --editable .
