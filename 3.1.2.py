#  Strings



'spam eggs'  # single quotes 
'doesn\'t'   # use \' to escape the single quote...
"doesn't"    # ...or use double quottes instead
'"yes," they said.'
"\"yes,\" they said."
'"Isn\'t," they said.'
# Interactive Interpreter
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'first line.\nSecond line.'  #\n means new;ine
s   # without print(), \n is included in the output
print(s)   # with print(), \n produces a new line

print('c:\some\name')   # here \n means new line!

print(r'C:\some\name')  # note the r before the quote



# Strings can be concatenated (glued together) with the + operator, and repeated with *:

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

'Py' 'thon'
# Output 'Python' 

# This feature is particularly useful when you want to break long strings:

text = ('put several strings wiithin parentheses '
        'to  have them joined together.')
text

# Output  'Put several strings within parentheses to have them joined together.'
