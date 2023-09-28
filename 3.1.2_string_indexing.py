# String can be indexed (subscripted), with the first character having index 0. There is no seperate character type; a character ia simply a string of one size:
word = 'Python'
word[0] # Character in position 0
# 'p'
word[5] # Character in position 5
# 'n'
# Indices many also be negative numbers, to satrt counting from the right:
word[-1] # last character
# 'n'
word[-2] # Second-last character
# 'o'
word[-6]
# 'p'
# [Note that -0 is same as 0, negative indices start from -1.]
# Attempting to use an index that is too large will result in an error:
word[42]  # the word only has 6 characters
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TndexError: string index out of range

# However, outof range slice indexes are handled gracefully when used for slicing:
word[4:42]
# 'on'
word[42:]
# ''


# Python string can not be changed __ they are immutable. Therefore, assigning to an index position in the string,, you should create a new one:
word[0] = 'j'


word[2:] = 'py'

# If you need a different string, you should create a new one:
'j' + word[1:]
# 'Jython'
word[:2] + 'py'
# 'Pypy'


