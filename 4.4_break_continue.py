# break and continue Statements, and clauses on Loops.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
# Loop fell through without finding a factor
        print(n, 'is prime number')



# Continue 
for num in range(2, 10):
    if num % 2 == 0:
        print ("Found an even number", num)
        continue
    print("Found an odd number", num)