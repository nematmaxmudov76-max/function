from typing import Callable

def decorator(func:Callable):
    count=0
    def wrapper():
        nonlocal count
        count+=1
        print(f"{count}-marta chaqirildi")
        func()
        print
    return wrapper
@decorator
def elon():
    print("hi dude")
elon()
elon()
