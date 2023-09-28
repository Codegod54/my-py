# Slicing is the extraction of a part of a string, list, or tuple.
# slicing allows to obtain substring:
word = 'Python'
word[0:2] # characters from position 0 (included) to 2 (excluded)
# 'Py'   output
word[2:5] # characters from position 2 (included) to 5 (excluded)
# 'tho'  output

# Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
word[:2] + word[2:]
# 'Python'
word[:4] + word[4:]
# 'Python'
# Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
word[:2]  # character from the begining to position 2 (excluded)
# 'Py'
word[4:]  # characters from position 4 (inncluded) to end
# 'on'
word[-2:] # character from the sexond-last (included) to the end 
# 'on'
