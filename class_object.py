class Student:                         # Class created
    school = 'Telusco'                 # Class variable or static
    def __init__(self, m1, m2, m3):    # Creating a function
        self.m1 = m1                   # Instance method (variable)
        self.m2 = m2                   # Instance method (variable)
        self.m3 = m3                   # Instance method (variable)

    def avg(self):                     # Creating function
        return (self.m1 + self.m2 + self.m3) / 3    # Average
    
    def get_m1(self):                  # Create function 
        return self.m1
    
    
s1 =student(34,67,32)                 # Object Crested
s2 =student(89,32,12)                 # Object Created

print(s1.avg())
print(s2.avg())