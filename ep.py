def this_fails():
    x = 1/0
    print(x)
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time err:', err)