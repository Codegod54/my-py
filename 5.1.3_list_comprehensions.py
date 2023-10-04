'''List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.'''
# For example, assume we want to create a list of squares, lke:

squares = []
for x in range(10):
    squares.append(x**2)    # Method 1
    squares = list(map(lambda x: x**2, range(10)))  # Method 2
    squares = [x**2 for x in range(10)] # Method 3
print(squares)

