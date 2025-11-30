from typing import Callable

def make_multiplier(n):
    return lambda  a: n*a
op=make_multiplier(3)
print(op(5))
op=make_multiplier(2)
print(op(4))
print(op(6))



