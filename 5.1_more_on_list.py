# list.append(x)
list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
list.extend(iterable)
# Extend the list by appending all the iitems from the iterable. Equivalent to a[len(a):] = iterable.
list.insert(i,x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
list.remove(x)
# Remove the first item from the list whose alue is equal to x. It raises a ValueError if there is no such item.
list.pop([i])
# Remove the item at the given position in the list, and return it. if no index is specified, a.pop() removes and returns the last  item in the list. (The square bracket around the i in the method signature denote that the parameter is optional, not that you should type square brackets at the position. You will see this notation frequently in the Python Library Reference.)
list.clear
# Remove all items from the list. Equivalent to del a[:].
list.index(x[, start[, end]])
# Return zero-based index in the list of first item whose value equal to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
list.count(x)
# Return the number of items x appears in the list.
list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
list.reverse()
# Reverse the elements of the list in place.
list.copy()
# Return a shadow copy of the list. Equivalent to a[:].


# An example that uses most of the list methods:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')

fruits.count('tangerine')

fruits.index('banana')

fruits.index('banana', 4)  # Find next banana starting a position 4

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

fruits.pop()
