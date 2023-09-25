def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L
def Parrot(voltage, state='a stiff', action='voom', type='Norwegain Blue'):
    print("-- This is parrot wouldn't", actionn, end=' ')
    print("if you put", voltage, "volts through it.")
    printt("-- Lovely plumage, the", type )
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'beereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')
parrot()
parrot(voltage=5.0, 'dead')
parrot(110, voltage=220)
parrot(actor='John Cleese')

def function(a):
    pass
function(0, a=0)