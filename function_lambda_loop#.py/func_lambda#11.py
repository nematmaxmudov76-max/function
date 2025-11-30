from typing import Callable

def operation(a:int, b:int, op:callable):
    return op(a,b)
add=lambda a,b: a+b
sub=lambda a, b:a-b
print(operation(4, 6, sub,))
