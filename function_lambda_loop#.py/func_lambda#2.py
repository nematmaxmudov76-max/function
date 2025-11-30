from typing import Callable

def add(x,y):
    return x+y

def suptract(x,y):
    return x-y

operation= [add, suptract]
a=int(input("a="))
b=int(input("b="))

for i in operation:
    print(i(a,b))

    