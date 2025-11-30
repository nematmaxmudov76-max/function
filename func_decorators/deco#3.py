from typing import Callable
def decorator(func:Callable):
    def wrp():
        print(func.__name__)
        func()
    return wrp
@decorator
def result():
    print("hi mate")
result()