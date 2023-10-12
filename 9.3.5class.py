# Correct design of the class should use an instance variable instead:
class Dog:

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fibo')
e = Dog('Buddy')
d.add_trick('roll oveer')
e.add_trick('play dead')

print(d.tricks)

print(e.tricks)