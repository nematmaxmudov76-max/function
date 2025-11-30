#1
# try:
#     a=int(input("a:"))
#     b=int(input("b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("nolga bo'lish mumkin emas!!!!!")
# except ValueError:
#     print("iltimos raqam kiriting!!")
# finally: print("tugadi 🤣")
#2
# def invert(l:list[int]):
#     try:
#         res=[i**(-1) for i in l]
#     except ZeroDivisionError:
#         print("listingizda nol bor ekan!")
#         return []
#     return res

# print(invert([1,3,5,6,8]))
# print(invert([-1,4,5,6,-5]))

# def invert(l:list[int]):
#     res=[]
#     for i in range(len(l)):
#         try:
#             res.append(l[i]**(-1))
#         except ZeroDivisionError:
#             print(f"l[{i}]= 0 ekan, tashlab ketaman")
#             continue
#     return res
# print(invert([1,3,4,6,7,8,9]))
# print(invert([1,3,-4,-7,8]))

#3
# try:
#     f= open("hello.txt", "r")
#     print(f.read())
# except FileExistsError:
#     print("fayl topilmadi")
# finally:
#     f.close()

#4
# def filtr(l:list):
#     res=[]
#     for i in range(len(l)):
#         try:
#             res.append(int([i]))
#         except ValueError:
#             print("listda intiger turiga mansub bo'lmagan abyektlar bor tashb ketyapman! ")
#             continue
#         return res
# print(filtr("1", '3', "5","8"))
# print(filtr('hi', "4","mate", '7'))

#5
# while True:
#     try:
#         n=int(input("n="))
#         print("thanks!")
#         break
#     except ValueError:
#         print("iltimos butun son kiriting")
#         continue

#6
# dic={
#     "ism":"toshmat",
#     "yosh":20,
#     "city":"toshkent"
# }
# while True:
#     try:
#         key=input("kalit kiriting;")
#         print(f"Kalit topildi:",dic[key])
#         break
#     except KeyError:
#         print("bunday kalit topilmadi!")
#     continue



#7
# from typing import Callable
# def decorator(func:Callable):
#     def wrapper(*args,**kwargs):
#         try:
#             print("funksiyaga murojat qilinyapdi")
#             func(*args,**kwargs)
#             print("funksiya to'g'ri!")
#         except ZeroDivisionError:
#             print("murojat qilingan funksiyada xatolik bor!!")
#     return wrapper
# @decorator
# def f():
#     print(1/9)
# f()

#8 IndexError
# l=[1,3,4,5,7,9,12]

# try:
#     index=int(input("Qaysi indexdagi son kerak:"))
#     print(f"{index}-index elemeti:",l[index])
# except IndexError:
#     print("bunday kalit topilmadi!")



#9
# l1=[1,2,3,4,5,6]
# l2=[3,4,5,6,7,8,9]
# maxlen=max(len(l1),len(l2))
# res=[]
# for i in range(0,maxlen):
#     try:
#         res.append(l1[i]/l2[i])
#     except IndexError:
#         print(f"list turlicha ekan keraksiz {i}- indexdan boshlab chopaman")
#         break
# print(res)


#11 
# while True:
#     try:
#         n=list(map(int, input("ro'yxat kiriting:").split()))
#         print("thanks!")
#         break
#     except ValueError:
#         print("iltimos butun son kiriting")
#         continue



#13 raqamlarni tahlil qilish => 3 bilan bir xil
# def filtr(l:list):
#     res=[]
#     for i in range(len(l)):
#         try:
#             res.append(int([i]))
#         except ValueError:
#             print("listda intiger turiga mansub bo'lmagan abyektlar bor tashb ketyapman! ")
#             continue
#         return res
# print(filtr("1", '3', "5","8"))
# print(filtr('hi', "4","mate", '7'))

#14
# flt=[]
# while True:
#     malumot=input("malumot kiritasizmi; Y/N  ")
#     if malumot=="Y":
#         try:
#             n=float(input("float kiriting:"))
#             if isinstance(n,int):
#                 raise TypeError("int turiga masub")
#             flt.append(n)
#             break
#         except TypeError:
#             print("iltimos float turiga mansub element kiriting!!")
#         except ValueError:
#             print('xatolik! son kiriting!!')
#     elif  malumot=="N":
#         break
# print(f"Kiritilgan malumotlar: ",flt)


#15 raise error




#20
# from typing import  Callable

# def decorator(func:Callable):
#     def wrapper(*args, **kwargs):
#         func(*args,**kwargs)
#     return wrapper

# def passord_checker(password:str):
#     if password != "eshmat":
#         raise PermissionError()



#21_______!!!
# def f{d:dict,key:str,value}:
#     try:
#         if not isinstance(d,dic):
#             raise TypeError("dict emas")
#         d[key]=value
#         return d
#     except TypeError:
    

#23_______!!!!
# def f(*args,):
#     try:
#         for i in args: 
#             if not isinstance(i,int):
#                 raise TypeError()
#         print(f(*args))
#     except TypeError:
#         print("neto satr kiritildi!")
# print(f('eshmat', "toshmat"))
# print(f("toshmat",23))

#24
# def filtr(l:list):
#     for i in range(len(l)):
#         try:
#             l[i]=int(l[i])
#         except: TypeError ("intga o'girib bo'lmadi")
       

# l=[1,2,3,4,'5', 'wp']
# filtr(l)
# for i in l:
#     print(i, type(i))


#25
# def filtr(l:list):
#     for i in range(len(l)):
#         try:
#             l=list(map(int,input().split()))
#             print("correct")
#         except: TypeError ("intga o'girib bo'lmadi")
# filter(l)

#26
# def f(l:list, index:int):
#     try:
#         print(l[index])
#     except IndexError:
#         print('xato')
# l=[1,2,3,4]
# f(l,5)





#28
# def downald():
#     return 'success'

# try:
#     data=downald()
#     if data=="failed":
#         raise Exception("no internet")
#     print(data)
# except:
#     print("xatolik, check in your network")

#29
# def f(k:int, l:int):
#     try:
#         print((lambda a,b: a/b)(k,l))
#     except ZeroDivisionError:
#         print('xatolik bor')
# print(f(1,0))
        

#30
# from typing import Callable
# def decorator(f:Callable, a:int,b:int):
#     try:
#         a=f(a,b)
#         print(a)
#     except ZeroDivisionError:
#         print("xatolik")
# print((lambda x,y:x/y)(1,0))


#31
# def exeption_log(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func()
#         except Exception as e:
#             print(f"error type: {type(e)}")
#     return wrapper
# @exeption_log
# def f():
#     print('I am working..')
#     raise PermissionError("this permisson error!")
# f()

#42

# def retry_on_failure(func):
#     def wrapper(*args,**kwargs):
#         for i in range(3):
#             try:
#                 func()
#             except ValueError as err:
#                 if i==2:
#                     raise ValueError(f"{i}-marta bu funksiyani amalga oshirolmadik")
#                 print(f"{i}-marta bu funksiyani amalga oshirolmadik")
#     return wrapper
# @retry_on_failure
# def myfunc():
#     raise ValueError("eshmat nima gap?")
# myfunc()
    







# k=map(int,input().split())
# d=(k*(k-3)/2)
# print(d)

#
from typing import Callable
def safe_call(func:Callable):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except ZeroDivisionError:
            print("bo'linishda xato yuz beridi")
        except Exception as e:
            print(f"boshqa xato yuz berdi:",{e})
    return wrapper
@safe_call
def f():
    import random
    l=[ZeroDivisionError,KeyError,TypeError]
    i=random.randrange(0,3)
    raise l[i]




# def butun_son(l:list):      
#     for i in range(len(l)):
#             if isinstance(l[i],int):
#                 res.append(l[i])
#                 print(f"ro'yxat:",res)
#                 raise Exception as e:
# print(butun_son([1,2,3,4,5,6,"st"]))

# def convert_exp(func):
#     def wrp(*args,**kwargs):
#         try:
#             func()    
#         except KeyError as e: #
#             raise ValueError(e)
#     return wrp
# @convert_exp
# def myfunc():
#     d={"ism":23, "city":"NWY"}
#     print(d["eshmat"])
