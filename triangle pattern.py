# triangle
# Left triangle star pattern
n = 5

for i in range(1, n+1):
    # internal loop run for i times
    for k in range(1, i+1):
        print("*", end="")
    print()

# Left triangle star pattern
n = 5

for i in range(1, n+1):
    # internal loop run for i times
    for k in range(1, i+1):
        print("*", end="")
    print()

#left side triangle
n =10
for i in range(1, n+1):
    print(" " * (n -i) + "*" * i)
