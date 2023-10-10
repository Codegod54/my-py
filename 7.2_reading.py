"""For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:"""

with open('workfile') as f:
    for line in f:
        print(line, end='')
# Reading all the lines 
        print(f.readlines())
        f.write('This is a test\n')

        value = ('the answer', 42)
        s = str(value)  # convert the tuple to string
        print(f.write(s))
        