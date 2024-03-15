# Constructor Overloading 
# It is a mechanism in which a class can have any number of constructors with different number of parameters & different type of parameters.

# Generally it is not possible.
# class Test:
#     def __init__(self,a):
#         print(a)
#     def __init__(self,a,b):
#         print(a)
#         print(b)
#     def __init__(self,a,b,c):
#         print(a)
#         print(b)
#         print(c)
# t=Test(10)  # Test.__init__() missing 2 required positional arguments: 'b' and 'c'
# t=Test(10,20)  # Test.__init__() missing 1 required positional argument: 'c'
# t=Test(10,20,30)  # It will always prior the last constructor.

# Constructor Overloading by using Multipledispatch module.
# from multipledispatch import dispatch
# class Test:
#     @dispatch(int)
#     def __init__(self,a):
#         print(a)
#     @dispatch(int,float)
#     def __init__(self,a,b):
#         print(a,b)
#     @dispatch(int,int,float)
#     def __init__(self,a,b,c):
#         print(a,b,c)
# t=Test(10)
# t=Test(10,2.55)
# t=Test(10,20,3.025)