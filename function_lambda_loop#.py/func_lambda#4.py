lambdas= [
   lambda x:x,
   lambda x:2*x,
   lambda x:3*x,
   lambda x:x*4,
   lambda x:x*5,
]
for i in lambdas:
    print(i(4))
    