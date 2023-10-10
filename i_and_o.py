s = 'hello, world.'

print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() o fa strinng adds string quotes and backlashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x,y, ('spam', 'eggs'))))