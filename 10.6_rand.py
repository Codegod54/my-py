"""The 'random' module provides tools for making random selections:"""

import random

p = random.choice(['apple', 'pear', 'banana'])
print(p)
q = random.sample(range(100),10)         # sampling without replacement 
print(q)
r = random.random()                      # random float
print(r)
s = random.randrange(6)                  # random integer chosen from range(6)
print(s)