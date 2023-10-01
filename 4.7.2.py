# Keyword Arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                    # 1 positional argument
parrot(voltage=1000)            # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')       # 2 keyword arguments
parrot(action='VOOOOOM', voltage=100000)        # 2 kkeyword arguments
parrot('a million', 'bereft of life', 'jump')   # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')        # 1 positional, 1 keyword

parrot()
parrot(voltage=5.0, 'dead')     # required argument missing 
parrot(101, voltage=220)        # duplicate value for the same argument
parrot(actor='John Ckeese')     # unknown keyword argument
# Fails due to restriction.
def function(a):
    pass
function(0, a=0)
