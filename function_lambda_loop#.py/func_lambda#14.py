from typing import Callable
numbers=map(int, input().split()) 
def filter_even(func:Callable,numbers:int):
    return func(numbers)
k=list(numbers)
sort=k.sort()
mx=max(k)
mn=min(k)

print(filter_even(mn,numbers))
print(filter_even(mx, numbers))
print(filter_even(sort, numbers))



