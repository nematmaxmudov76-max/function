from typing import Callable

def decorator(func:Callable):
    def wrapper(*args):
        print("Starting..")
        func()
        print("Down..")
    return wrapper

@decorator
def elon():
    print("hi")
elon()
