# 1.Single Inheritance

# Child class can access own members as well as Parent class members but Parent class can access only own members.
# class A:
#     def method1(self):
#         self.i=10
#         print(f'I value is {self.i}')
#     def method2(self):
#         self.j=20
#         print(f'J value is {self.j}')
# class B(A):
#     def method3(self):
#         self.x=50
#         self.y=60
#         print(f'X value is {self.x}')
#         print(f'Y value is {self.y}')
# b=B()
# b.method1()
# b.method2()
# b.method3()
# a=A()
# a.method1()
# a.method2()
# a.method3()  # AttributeError: 'A' object has no attribute 

# If we will do any modification in Child class it will not reflect to Parent class.
# class A:
#     def method1(self):
#         self.i=10  
# class B(A):
#     def method2(self):
#         self.i=999  # inside Child class updated i value
# a=A()
# a.method1()
# print(a.i)
# b=B()
# b.method1()
# b.method2()
# print(b.i)

# -------------------------------------------------------------

# Multi-Level Inheritance

# A class is derived from a class which is already derived from another class.
# class A:
#     def method1(self):
#         print('Parent class Method 1')
# class B(A):
#     def method2(self):
#         print('Child class Method 2')
# class C(B):
#     def method3(self):
#         print('Grand-Child class Method 3')
# c=C()
# c.method1()
# c.method2()
# c.method3()

# -----------------------------------------------------------------

# 3.Hierarchical Inheritance

# Here multiple classes are derived from a single class
# class A:
#     def method1(self):
#         print('Parent class Method 1')
# class B(A):
#     def method2(self):
#         print('Child class Method 2')
# class C(A):
#     def method3(self):
#         print('Child class Method 3')
# b=B()
# b.method1()
# b.method2()
# # b.method3()  # AttributeError: 'B' object has no attribute 'method3' 
# c=C()
# c.method1()
# c.method3()
# # c.method2()  # AttributeError: 'C' object has no attribute 'method2'

# ----------------------------------------------------------------------

# 4.Multiple Inheritance

# Here one class is derived from multiple classes. It means one child have multiple parents.
# class A:
#     def method1(self):
#         print('A Parent class Method 1')
# class B:
#     def method1(self):
#         print('B Parent class Method 1')
# class C(A,B):  # here A is the first parent so A class print statement will come
#     pass
# c=C()
# c.method1()
# class D(B,A):  # here B is the first parent so B class print statement will come
#     pass
# d=D()
# d.method1()

# Ambiguity Problem(Based on priority of class output will come)
# class A:
#     def method1(self):
#         print('A class Method 1')
# class B:
#     def method1(self):
#         print('B class Method 1')
# class C(A,B):
#     def method1(self):
#         print('C class Method 1')
# c=C()
# c.method1()  # C class Method 1

# -------------------------------------------------------------------------------

# 5.Hybrid Inheritance(Collection of more than one Inheritance)

# Diamond shape problem
# class A:
#     def method1(self):
#         print('A class Method 1')
# class B(A):
#     def method2(self):
#         print('B class Method 2')
# class C(A):
#     def method3(self):
#         print('C class Method 3')
# class D(B,C):
#     def method4(self):
#         print('D class Method 4')
# d=D()
# d.method1()
# d.method2()
# d.method3()
# d.method4()

# ----------------------------------------

# Cyclic Inheritance

# It is not supported in python & it is not required.
# class A(A):  # NameError: name 'A' is not defined
#     def method(self):
#         print('A class method')  

# class A(B):  # NameError: name 'B' is not defined
#     def method1(self):
#         print('A class Method 1')
# class B(A):
#     def method2(self):
#         print('B class Method 2')
# a=A()
# b=B()
# a.method1()
# b.method1()
# b.method2()