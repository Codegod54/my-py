# Instance Variable 

"""
* Instance variable are specific to each instance of a class. They are defined within the methods of the class, often in the constructor ('__init__'  method).

* Instancce variables are unique to each instance and can have different values for each instance.

* They are accessed using the instance name (usually 'self') within the methods of the class.
"""
class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # This is an instance variable

obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

print(obj1.instance_variable)  # Accessing instance_variable for obj1
print(obj2.instance_variable)  # Accessing instance_variable for obj2