#2
# from typing import Callable

# def decorator(func):
#     count=0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count+=1
#         print("hiii")
#         func(*args,**kwargs)
#         print("hello world")
#     return wrapper
# @decorator
# def myfunc(*args,**kwargs):
#     print(args,kwargs)
# myfunc(5)


# def decorator(func):
#     def  wrapper(*args,**kwargs):
#         print(func._name_)
#         func()
# @decorator
# def salom():
#     print("salom!")
# salom()


#4
# def decorator(func):

#     def wrapper(*args, **kwargs):
#         ret= func(*args,**kwargs)
#         print(ret.upper())
#     return wrapper
# @decorator
# def salom_ber(s:str):
#     return "salom "+s
# salom_ber("eshmat")



#5
# def decorator(func):
#     def wrapper(s:int):
#         if s>0:
#             print("musbat!")
#         if s<0:
#             print("manfiy!")
#             return
#         func(s)
#     return wrapper
# @decorator
# def myfunc(s:int):
#     print()
# myfunc(4)



#12
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         l= args[0]
#         k=set(l)
#         func(k)
#     return wrapper
# @decorator
# def myfunc(lst: list[int]):
#     print(f"list",lst )
# myfunc([1,2,4,4,6,7,7,9])




#15 error
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         l= args[0]
#         for i in args:
#             if i<=0:
#                 print("manfiy!!!!")
#                 return
#         func(*args)
#     return wrapper
# @decorator
# def myfunc(*args):
#     print(args)

# print(1,2,4,6,8,3)
# print(1,4,-3,5,8)





# # cash bilan ishlash
# def cashe(func):
#     last_call=dict()
#     def wrapper(*args, **kwargs):
#         nonlocal last_call
#         print(last_call)
#         s=args[0]
#         if s in last_call:
#             return last_call[s]
#         else:
#             res=func(s)
#             if len(last_call)>2:
#                 last_call.popitem(list(last_call.keys()))
#                 last_call[s]=res
#     return wrapper

# @cashe
# def say_hi(s:str):
#     return 
# print(say_hi("eshmat"))
# print(say_hi("toshmat"))
# print(say_hi("gishmat"))
# print(say_hi("axmat"))
# print(say_hi("eshmat"))


# from typing import Callable

# def tyrFly(func:Callable):
#     def wrapper():
#             print("tayyor")
#             func()
#             print("uchdi")
#     return wrapper

# @tyrFly
# def countDown():
#          for i in range(10,0,-1):
#             print(i)

# countDown()


# from typing import Callable

# def decorator(func:Callable):
#     def wrapper(*args):
#         print("Starting..")
#         func()
#         print("Down..")
#     return wrapper

# @decorator
# def elon():
#     print("hi")
# elon()



#3
# from typing import Callable

# def decorator(func:Callable):
#     count=0
#     def wrapper():
#         nonlocal count
#         count+=1
#         print(f"{count}-marta chaqirildi")
#         func()
#         print
#     return wrapper
# @decorator
# def elon():
#     print("hi dude")
# elon()
# elon()

#4
# from typing import Callable

# def decorator(func:Callable):
#     def wrapper(*args,**kwargs):
#         a=func(*args,**kwargs)
#         return a.upper()
#     return wrapper

# @decorator

# def res(s:str):
#     return 'hi '+ s

# res('eshmat')


# #8
# from typing import Callable

# def decorator(func:Callable):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             print(type(i))

#         for val in kwargs.values():
#             print(tuple(val))

#         return func(args,kwargs)
    
#     return wrapper
# @decorator
# def res(*args):
#     return 
# res(2,"hi",False,  )


#9
# from typing import Callable
# def decorator(func:Callable):
#     def wrapper(*args):
#         for i in range(3):
#             print("hi mate")
#         return func
#     return wrapper
# @decorator
# def res():
#     return 
# res()


# #11
# from typing import Callable
# def decorator(func:Callable):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         if res is None:
#             return "no result"
#         return  func(*args,**kwargs)
#     return wrapper
# @decorator
# def res():
#     return "osh"
# res()

#12
# from typing import Callable
# def decorator(func:Callable):
#     def wrp(*args,):
#         even=[]
#         for i in args:
#             if args%2==0:
#                even.append(args)
#         func(*tuple(even)) #list ko'rinishida berolmaymiz agar * bo'lmasa qo'ydik
       
#     return wrp

# @decorator
# def res(*n):
#     return n
# res(1,3,5,6,6,7)


#15
# from typing import Callable
# def decorator(func:Callable):
#     count=0
#     def wrp(*args,):
#         nonlocal count
#         count+=1
#         if count<6:
#             func(*args)
#         else:
#             print("ortib ketdi")
#             return
        
#         return  



#