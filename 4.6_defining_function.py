# Defining function
# We can create a function that writes the fibonacci series to an arbituary boundary:
def fib(n):     # write Fibonacci series up to n
    """Print  a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

# Now call the fuunction we just defined:
fib(2000)

fib

f = fib
f(100)

fib(0)
print(fib(0))

def fib2(n):    # returns Fibonacci series up to n
    """Returns a list conatainig the fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)        #see below
    return result
f100 = fib2(100)        # call it 4
print(f100)                  # write the result

