# Finding odd even number in range.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(num1, num2):
        if i % 2 == 0:
            print("It is even number:", i)
            continue
        print("It is odd number:", i)