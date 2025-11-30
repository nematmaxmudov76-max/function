from typing import Callable
def decorator(func:Callable):
    def wrapper(*args,**kwargs):
        for arg in args:
            if isinstance(arg, str) and arg=="":
                print("argument bo'sh")
                return
        return func(*args,**kwargs)
    return wrapper
@decorator
def res(s:str):
    print(f"ishga tushdi",{s})
res("")
res("hi mate")
