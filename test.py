vec = [-4, -2, 0, 2, 4]
# Create a new list with the values doubled
print([x*2 for x in vec])
# Filter the list to exclude negative numbers
print([x for x in vec if x>= 0])
# Apply a function to all the elements
print([abs(x) for x in vec])
# Call a method in all element
freshfruit = [' banana  ', '  loganberry', 'passion fruit ']
print([weapon.strip() for weapon in freshfruit])
# Create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(10)])
# The tuple must be parenthesized, otherwise an error is raised
print([x, x**2 for x in range(6)])
# flattern a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])