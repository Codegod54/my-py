# performance Measurement

from timeit import Timer

per1 = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(per1)

per2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(per2)