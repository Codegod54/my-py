# Local Scope

"""
Variable declared within a function are in the local scope of that function.

Only accessible within that specific function.
"""


def my_function():
    local_variable = 10
    print(local_variable)

my_function()

#This would raise an error because local_variable is not defined in this scope
# print(local_variable)  