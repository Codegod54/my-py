# Saving structured data with json
import json
print(json.dumps([1, 'simple', 'list']))

# another variant of the dumps() function, called dump(), simply searilizes the object to a text file . So if f is a text file object opened for writing, wecan do this:
json.dump(x, f)

# To decode the object again, if f is a text file object which has been opened for reading:
x = json.load(f)
