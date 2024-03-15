# variable length keyword argument

# issues
# def fun(**a):
#     print(a)
# fun(10,20)  # TypeError: fun() takes 0 positional arguments but 2 were given

# solutions
# def fun(**a):
#     print(a)
# fun(x=10,y=20)  
# it stores the data in the form of Dictionary.

# def fun(**a):
#     print(a)
# fun(x=10,y=20.30,z=[10,20,30],z1={1:2,2:3})  

# def fun(x,**a):
#     print(x)
#     print(a)
# fun(x=99,a=10,b=20,c=30)  

# def fun(x,**a):
#     print(x)
#     print(a)
# fun(a=10,b=20,c=30,x=99)  

# def fun(x,*y,**z):
#     print(x)
#     print(y)
#     print(z)
# fun(99,a=10,b=20,c=30) 

# def fun(x,*y,**z):
#     print(x)
#     print(y)
#     print(z)
# fun(99,77,88,a=10,b=20,c=30)   

# first we have to use variable length non-keyword argument then variable length keyword argument otherwise we gets a systaxerror.
# def fun(x,**y,*z):
#     print(x)
#     print(y)
#     print(z)
# fun(99,77,88,a=10,b=20,c=30)  # SyntaxError

# def fun(**a):
#     print(a)
# fun()
# fun(x={})

# def fun(*a,**b):
#     print(a)
#     print(b)
# fun(x=10,y=20,30,40,50)  # SyntaxError: positional argument follows keyword argument