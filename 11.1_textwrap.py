""""
The textwrap module formats paragraphs of text to fit a given screen width:
"""

import textwrap

doc = """the wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to seperaate the wrapped lines."""

print(textwrap.fill(doc, width = 40))
