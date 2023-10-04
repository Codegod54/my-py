"""
It is possible to use lists as a queue, where the first element adds is the first element retrived ("first-in, first-out"); however, lists are not efficiemt for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the end of the list are fast, doing inserts or pops from the begining of a list is shown (because all of the other elements have to be shifted by one).


To implement queue, use collections.deque which was designed to have fast appends and pops from both ends.
"""
# For example:
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves

print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival
