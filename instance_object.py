# Creating Instance Objects


# Creating Class:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating Instance Objects:

person1 = Person("Alice", 30)

person2 = Person("Bob", 25)


# Assigning Attributes and Methods:

print(person1.name) # Accessing the 'name' attribute of person1

person2.greet() # Calling the 'greet' method on person2

