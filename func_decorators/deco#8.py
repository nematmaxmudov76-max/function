from typing import Callable

def decorator(func:Callable):
    def wrapper(*args, **kwargs):
        for i in args:
            print(type(i))

        for val in kwargs.values():
            print(tuple(val))

        return func(args,kwargs)
    
    return wrapper
@decorator
def res(*args):
    return 
res(2,"hi",False,  )



from typing import Callable

def decorator(func:Callable):
    def wrapper(*arsg, **kwargs):
        print(type(arsg,))
        return
    return wrapper
@decorator
def res():
    return
res(2)
