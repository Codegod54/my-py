# method Objects
# Creating an Class with Methods

class MyClass:

    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

    def double_value(self):
        self.value *= 2

# Create an Instance:

obj = MyClass(5)

# Method Objects:

print_method = obj.print_value # Store the print_value method as a method object
double_method = obj.double_value # Store the double value methods as a method object.


# Call the Method Objects:

print_method () # Calls the print_value method on 'obj' which prints the value (5)

double_method () # Calls the double_value method on 'obj', doubling the value to 10

