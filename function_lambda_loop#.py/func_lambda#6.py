from typing import Callable

def operation(
        x:int,
        y:int,
        func:Callable
):
    return func(x,y)
print(operation(4,7, lambda x, y: x-y))
