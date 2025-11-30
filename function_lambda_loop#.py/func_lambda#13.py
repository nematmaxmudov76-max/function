from typing import Callable
x=int(input("x="))
def select_func(name):
    return name
square = x**2
cube = x**3
double = x*2
print(select_func(cube))
print(select_func(double))
print(select_func(square))
