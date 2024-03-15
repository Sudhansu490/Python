# uses of * in function() call

# def fun(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# l=[10,20,30]
# fun(*l)

# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# l=[10,20,30]
# fun(*l)  # TypeError: fun() missing 1 required positional argument: 'z'

# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# l=[10,20,30]
# fun(*l,77) 

# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# l=[10,20,30]
# fun(77,*l) 

# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# l=[10,20,30]
# fun(77,99,*l)  # TypeError: fun() takes 4 positional arguments but 5 were given

# we can also us Tuple.
# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# t=(10,20,30,40)
# fun(*t)

# we can also us Set.
# def fun(a,x,y,z):
#     print(a)
#     print(x)
#     print(y)
#     print(z)
# s={10,20,30,40}
# fun(*s)

# ----------------------------------------------------------

# uses of ** in function() call

# def fun(a,**s):
#     print(a)
#     print(s)
# fun(10,i=20)

# def fun(a,**s):
#     print(a)
#     print(s)
# d={'i':2,'j':3,'k':4}
# fun(10,**d)