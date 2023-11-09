# Nonloocal Scope

"""
Used whennn you have a nested function and you want to modify a variable in the enclosing (non_global) scope.

The 'nonlocal' keyword is used for this.
"""

def outer_function():
    outer_variable = 5

    def inner_function():
        nonlocal outer_variable
        outer_variable = 20

    inner_function()
    print(outer_variable)

outer_function()
