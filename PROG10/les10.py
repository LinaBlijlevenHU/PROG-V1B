def f(b):       # f has global scope, b has local scope
    return a*b  # this a is the global a

a = 0           # this a has global scope
print('f(3) = {}'.format(f(3)))
print('a is {}'.format(a))        # global a is still 0

