# Variable Length Non-Keyword Argument(*args)

# issues or problems

# def fun(a,b,c,d,e):
#     print(a,b,c,d,e)
# fun(10,20,30,40,50,60,70)  # Error

# solutions

# def fun(*a):
#     print(a)
# fun(10)
# fun(10,20,30,40,50,60,70)
# fun() 
# it stores the data in the form of Tuple Data Structure.

# def fun(*args):
#     print(args)
# fun(10,20,[30,40],50.50,60+70j,True)

# ------------------------------------------------

# variable length keyword argument + positional argument

# def fun(x,*a):
#     print(x)
#     print(a)
# fun(10,20,30,40)

# def fun(x,*a):
#     print(x)
#     print(a)
# fun(10,20,30,x=40)  # TypeError: fun() got multiple values for argument 'x'

# if we take first *a then positional argument in the parameter then fun() missing required arguments
# def fun(*a,x):
#     print(x)
#     print(a)
# fun(10,20,30,40)  # TypeError: fun() missing 1 required keyword-only argument: 'x'

# def fun(*a,x): 
#     print(x)
#     print(a)
# fun(10,20,30,x=40)

# as positional argument follows keyword argument so below code shows error.
# def fun(*a,x): 
#     print(x)
#     print(a)
# fun(x=40,10,20,30)  # Error

# def fun(*a,x):
#     print(a)
#     print(x)
# fun(x=40)

# Premium Point => After variable length argument if we want to pass other argument then we can pass by providing value as keyword argument.

# -----------------------------------------------------------------------------

# variable length keyword argument + default argument

# def fun(*a,x=10):
#     print(a)
#     print(x)
# fun(99)

# def fun(*a,x=10):
#     print(a)
#     print(x)
# fun(10,20,30,40,50,x=99)

# def fun(x=10,*a):
#     print(a)
#     print(x)
# fun(10,20,30,40,50,x=99)  # TypeError: fun() got multiple values for argument 'x'

# def fun(x=10,*a):
#     print(a)
#     print(x)
# fun(99,10,20,30,40,50)

# ---------------------------------------------

# variable length keyword argument + positional argument + default argument

# def fun(a,*b,c=99):
#     print(a)
#     print(b)
#     print(c)
# fun(10)

# def fun(a,*b,c=99):
#     print(a)
#     print(b)
#     print(c)
# fun(10,20,30,40,c=77)

# def fun(a,b=99,*c):
#     print(a)
#     print(b)
#     print(c)
# fun(10,20,30,40,b=77)  # TypeError: fun() got multiple values for argument 'b'

# def fun(a=99,b,*c):
#     print(a)
#     print(b)
#     print(c)
# fun(10,20,30,40)  # SyntaxError: non-default argument follows default argument