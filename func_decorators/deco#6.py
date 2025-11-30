from typing import Callable

def decorator(func:callable):
    def wrp(*args, **kwargs):
        for arg in args:
            if arg<0:
                print("manfiy son!")
                return None
        return func(*arg, **kwargs)
    return wrp
@decorator
def res(*r):
    print("musbat son!")
res(1,2,4,6)