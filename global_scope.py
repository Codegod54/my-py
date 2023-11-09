# Global Scope

"""
Variable declared outside of any function or block are in the global scope.

Accessible from anywhere in the code, both inside and outside functions.
"""

global_vaariable = 42

def my_function():
    print(global_vaariable)

my_function()

