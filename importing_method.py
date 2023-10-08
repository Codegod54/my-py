from fibo import fib, fib2      # Importing each name seperately.
print(fib(500))

from fibo import *      # Importing all the name at once.
print(fib(500))

import fibo as fib      # importing and assigning its module name as fib.
print(fib.fib(500))

from fibo import fib as fibonacci       # Importing module and assigning its function name as fibonacci
print(fibonacci(500))