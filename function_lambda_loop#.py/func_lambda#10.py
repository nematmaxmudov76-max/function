def choos(condition):
    if condition:
        return lambda x: x+10
    else:
        return lambda x: x-10
res=input("t/f: ")
if res=="t":
    k=True
else:k=False
func=choos(k)
print(func(5))
