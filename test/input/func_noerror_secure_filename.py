'''Ensure that pylint finds the exported methods from Werkzeug.'''

from werkzeug import secure_filename

MYFILE = secure_filename("mycoolfile")
