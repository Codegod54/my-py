# Output Formatting
"""The reprlib module provides a version of repr() customized for abbreviated displays of large or deeply nested containers:"""


import reprlib
rep = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(rep)