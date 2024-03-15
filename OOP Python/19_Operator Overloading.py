# Operator Overloading(uses of same operator for different purposes)
# We are using +,* etc. operators are for different purposes.

# Operator Overloading without using Magic Method(Not Possible)
# class Employee:
#     def __init__(self,esal):
#         self.esal=esal
# class Student:
#     def __init__(self,pkt_money):
#         self.pkt_money=pkt_money
# e=Employee(10000)
# s=Student(5000)
# print(e+s)  # TypeError
# here we are trying to add two reference variables which is not possible without Magic Method.

# Operator Overloading by using Magic Method

# Ex=1(addition)
# class Employee:
#     def __init__(self,esal):
#         self.esal=esal
#     # Magic Method
#     def __add__(self,other):
#         return self.esal+other.pkt_money
# class Student:
#     def __init__(self,pkt_money):
#         self.pkt_money=pkt_money
# e=Employee(15000)
# s=Student(5000)
# print(e+s)
# Whenever,we are trying to add two objects python will automatically execute the Magic Method.

# Ex=2(check which one greater & smaller)
# class Employee:
#     def __init__(self,esal):
#         self.esal=esal
#     def __gt__(self,other):
#         return self.esal>other.pkt_money
#     def __lt__(self,other):
#         return self.esal<other.pkt_money
# class Student:
#     def __init__(self,pkt_money):
#         self.pkt_money=pkt_money
# e=Employee(15000)
# s=Student(5000)
# print(e>s)
# print(e<s)

# Ex=3(write a class complex to represent complex numbers, along with overloaded operators + & * which adds & multiplies them.)
# (a+bi)(c+di)=(ac-bd) + (ad+bc)i
# class Complex:
#     def __init__(self,i,r):
#         self.imaginary=i
#         self.real=r
#     def __add__(self,c):
#         return Complex(self.real+c.real,self.imaginary+c.imaginary)
#     def __mul__(self,c):
#         mulReal=self.real*c.real - self.imaginary*c.imaginary
#         mulImag=self.real*c.imaginary + self.imaginary*c.real
#         return Complex(mulReal,mulImag)
#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real} - {-self.imaginary}i"
#         else:
#             return f"{self.real} + {self.imaginary}i"
# c1 = Complex(1, -4)
# c2 = Complex(331, -37)
# print(c1 + c2)
# print(c1 * c2)