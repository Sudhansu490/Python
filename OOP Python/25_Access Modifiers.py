# Access Modifiers are used to control the scope of attributes & methods.

# -----------------------------------------------------------------------

# 1.Public(Anyone can access at anywhere)

# Attributes
# class A:
#     def __init__(self):
#         self.x=23  # Public Attribute
#     def test(self):
#         print(self.x)  # accessing public attribute within the class
# class B(A):
#     def test1(self):
#         print(self.x)  # accessing public attribute within the child class 
# a=A()
# a.test()
# b=B()
# b.test1()
# print(a.x)

# Methods
# class A:
#     def mt1(self):  # public method
#         print('mt1 Method')
#     def demo(self):
#         self.mt1()
# class B(A):
#     def test(self):
#         self.mt1()
# a=A()
# a.demo()  # calling Public method inside the class
# a.mt1()  # calling Public method outside the class
# b=B()
# b.test()  # calling Public method inside child class

# -----------------------------------------------------------------------------------

# 2.Protected(within the class we can access & within child class also we can access but we can't access outside of the class)
# '_' symbol is used to create Protected access modifier.

# Attributes
# class A:
#     def __init__(self):
#         self._x=23  # Protected Attribute
#     def test(self):
#         print(self._x)  # accessing Protected Attribute within the class 
# class B(A):
#     def test2(self):
#         print(self._x)  # accessing Protected Attribute within the child class
# a=A()
# a.test()
# b=B()
# b.test2()
# print(a._x)  # accessing Protected Attribute outside of the class(Generally it is not possible)
# NOTE- Python doesn't provide  support for Protected modifiers.It is just a naming convention.

# Methods
# class A:
#     def _m1(self):
#         print('I am Protected method')
#     def demo(self):
#         self._m1()
# class B(A):
#     def m2(self):
#         self._m1()
# a=A()
# a.demo()  # calling Protected method inside the class
# b=B()
# b.m2()  # calling Protected method inside the child class
# a._m1()  # calling Protected method outside the class(Generally it is not possible)

# # -------------------------------------------------------------------------------------

# 3.Private(only within the class it is possible)
# NOTE-: '__' symbols is used to define Private Access Modifiers.

# Attributes
# class A:
#     def __init__(self):
#         self.__x=25  # Private Attribute
#     def demo(self):
#         print(self.__x)  # accessing Private attribute within the class
# class B(A):
#     def test(self):
#         print(self.__x)  # accessing Private attribute within the child class(Impossible)
# a=A()
# a.demo()
# b=B()
# b.test()
# print(a.__x)  # accessing Private attribute outside of the class(Impossible)

# Methods
# class A:
#     def __mt1(self):
#         print('I am Private method')  # Private method
#     def demo(self):
#         self.__mt1()  # accessing Private method within the class
# class B(A):
#     def test(self):
#         self.__mt1()  # accessing Private method within the child class(Impossible)
# a=A()
# a.demo()
# b=B()
# b.test()
# a.__mt1()  # accessing Private method outside of the class(Impossible)

# ------------------------------------------------------------------------------------

# class A:
#     def __init__(self):
#         self.__p=25
# a=A()
# print(a.__p)  # directly it is not possible
# print(a._A__p)  # Name mingling