# Object

"""
Object is a physical or reaal entity that works on class data.

Note:
1) Each object has a distinct role or responsibility.
2) Object creates space on memory as per class members.
"""
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)