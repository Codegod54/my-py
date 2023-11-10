# Class Variable 
"""
* Class variables are shared among all instances of a class. They are associated with the class itself, onot with any perticular instance.

* Class variable are declared within the class but outside of any methods, typically at the top of the class defination.

* They are assigned using the class name, not an instance, although you can also acceses them through an instance.
"""
class MyClass:
    class_variable = 0  # This is a class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # This is an instance variable


print(MyClass.class_variable)