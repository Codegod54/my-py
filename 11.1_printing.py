"""
The 'pprint' module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by interpreter.
"""

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)

