from typing import Callable
def decorator(func:Callable):
    def wrapper(*args):
        for i in range(3):
            print("hi mate")
        return func
    return wrapper
@decorator
def res():
    return 
res()