from typing import Callable

def apply(func:Callable, nums:list[int]):
    for i in range(len(nums)):
        nums[i]=func(nums[i])
    return nums

nums=[1,2,3,4,5]
print(apply(lambda x: x*x, nums))
print(nums)
