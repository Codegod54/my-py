def bool_return():
    try:
        return True 
    finally:
        return False
print(bool_return())

# A more complicated example:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")              # Cathes exception wich is not divisible by Zero.
    else:
        print("result is", result)              # Prints result if no exception is found.
    finally:
        print("executing finally clause")       # Executes either the use of resource is successful.
    
divide(2, 1)
divide(2, 0)
divide("2", "1")
 