from typing import Callable
def decorator(func:Callable):
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        if res is None:
            return "no result"
        return  func(*args,**kwargs)
    return wrapper
@decorator
def res():
    return "osh"
res()