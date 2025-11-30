from typing import Callable

def decorator(func:Callable):
    def wrapper(string):
        a=func(string)
      
        return a.uppper()
    return wrapper

@decorator

def res(s):
    return s

res('eshmat')
