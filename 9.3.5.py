# Class and Instance Variables
class Dog:              # Class created
    kind = 'canine'     # Class variable shared by all instances

    def __init__(self, name):   # Defining function
        self.name = name    # Insatnce variable unique to each instance

d = Dog('Fido')         # Object created
e = Dog('Buddy')        # Object created
print(d.kind)           # Shared by all dogs
print(e.kind)           # Shared by all dogs

print(d.name)           # Unique to d
print(e.name)           # Unique to e
