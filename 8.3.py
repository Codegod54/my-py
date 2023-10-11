# Handling Exceptions 
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Opps! That was no valid number. Try again...")
    except (RuntimeError, TypeError, NameError):
        pass
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")