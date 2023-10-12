# Random Remarks
class Warehouse:        # class created
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()        # object 1
print(w1.purpose, w1.region)

w2 = Warehouse()        # oobject 2
w2.region = 'east'      # changes the variable of region 
print(w2.purpose,   w2.region)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x + y)

class c:
    f = f1

    def g(self):
        return 'hello world'
    
    h = g

# Methods may call other methods by using method attributes of the self argument:

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
         