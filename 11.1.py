# Output Formatting
"""The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:"""


import reprlib
rep = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(rep)


"""
The 'pprint' module offers more sophisticated control over printing both built-in and user defined objects in a way that is readable by interpreter.
"""

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)


""""
The textwrap module formats paragraphs of text to fit a given screen width:
"""

import textwrap

doc = """the wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to seperaate the wrapped lines."""

print(textwrap.fill(doc, width = 40))



"""
The locale module accesses a database of culture specific data formats. The grouping attribute of locale’s format function provides a direct way of formatting numbers with group separators:
"""

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()                  # get a mappijnng of conventions
x = 1234567.8
locale.format("%d", x, grouping )