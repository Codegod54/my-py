# To iterate over the indices of a sequence, you can combine range() and len() function as follows:
a = ['Marry', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    # i is printed and the content and incremented and again printed in a loop
    print(i, a[i])
print(list(enumerate(a)))

print(range(10))

print(sum(range(4))) # 0 + 1 + 2 + 3
# output = 6

print(list(range(4)))
# output = [0, 1, 2, 3]