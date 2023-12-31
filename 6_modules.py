# Fibonacci numbers module

def fib(n):     # write fibonacci series up ti n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # return fibonacci series up to n 
    result = [ ]
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result
    
import fibo

fibo.fib(1000)

fibo.fib2(100)

fibo.__name__

fib = fibo.fib
fib(500)
