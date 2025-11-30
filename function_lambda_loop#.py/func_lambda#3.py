def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mull(x,y):
    return x*y

d={
    "add":add,
    "sub":sub,
    "mul":mull
}
x=int(input("x="))
y=int(input("y="))
operation=input(["add","sub","mull"])
print(d[operation](x,y))
