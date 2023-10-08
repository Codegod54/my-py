import fibo
print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

# Assigning it to a local name.
fib = fibo.fib
print(fib(500))
print(fib.__name__)