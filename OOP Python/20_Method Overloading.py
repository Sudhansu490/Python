# Method Overloading(methods with same name but different number of parameters & different type of parameters)

# class Test:
#     def mt1(self,a):
#         print(a)
#     def mt1(self,a,b):
#         print(a)
#         print(b)
#     def mt1(self,a,b,c):
#         print(a)
#         print(b)
#         print(c)
# t=Test()
# t.mt1(10)  # Test.mt1() missing 2 required positional arguments: 'b' and 'c'
# t.mt1(10,20)  # Test.mt1() missing 1 required positional argument: 'c'
# t.mt1(10,20,30)
# Python doesnot support Method Overloading.

# how to achieve method overloading
# class Test:
#     def mt1(self,*a):
#         print(a)
# t=Test()
# t.mt1(10)
# t.mt1(10,20)
# t.mt1(10,20,30,40)
# Another type
# class Test:
#     def mt1(self,a=None,b=None):
#         print(a)
#         print(b)
# t=Test()
# t.mt1()
# t.mt1(10)
# t.mt1(10,20)

# Method Overloading by using Multiple Dispatch Decorator.
# from  multipledispatch import dispatch
# class Test:
#     @dispatch(int,int)
#     def add(a,b):
#         print(a+b)
#     @dispatch(int,float)
#     def add(a,b):
#         print(a+b)
#     @dispatch(float,float)
#     def add(a,b):
#         print(a+b)
#     @dispatch(int,float,int)
#     def add(a,b,c):
#         print(a+b+c)
# t=Test()
# t.add(10,20)
# t.add(10,5.55)
# t.add(7.25,6.45)
# t.add(15,3.05,45)