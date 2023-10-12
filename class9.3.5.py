# A Word About Names and Objects

class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name    # instance variable

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fibo')
e = Dog('Buddy')
d.add_trick('roll oveer')
e.add_trick('play dead')

print(d.tricks)            # unexpectedly shared by all dogs
 