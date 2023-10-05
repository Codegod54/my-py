# Looping through dictionaries.
knights = {'gallahad': 'the pure', 'robin': 'the brve'}
for k, v in knights.items():
    print(k, v)

# Looping through a sequence.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# To loop over two or more sequences at the same time.

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0}? It is {1}.'.format(q, a))

# To loop over a sequence in reverse.

for i in reversed(range(1,10,2)):
    print(i)

# To loop over a sequence in sorted order.

basket = ['apple', 'orange', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)