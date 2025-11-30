from typing import Callable

def apply(func: callable, value:int):
    return func(value)

print(apply(lambda x:x**2, 4))
