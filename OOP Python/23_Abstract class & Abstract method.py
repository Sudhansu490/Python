# Partial implementation of a class is called as Abstract class.
# Abstract class is the blueprint of other classes.
# Abstract class contain at least 1 Abstract method.
# Python doesnot provide support for Abstract class, so we have to import a module named as abc module.
# abc module stands for abstract base class.
# Abstract class can also contain Concrete method

# A method without having body part is called as Abstract method.
# If we don't know the body part of method then at that time we can define Abstract method.
# By using @abstractmethod decorator we can define Abstract method.
# Child class will provide the body part of Abstract method.
# We can't create the object for Abstract class.

# A Method having body part is call Concrete method.

from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def area(self,r):
#         print(f'Area of Circle is {3.14*r*r}')
# class Square(Shape):
#     def area(self,s):
#         print(f'Area of Square is {s*s}')
# c=Circle()
# c.area(5)
# s=Square()
# s.area(10)

# An Abstract class contain Abstract method as well as Concrete method.
# class Car(ABC):
#     @abstractmethod
#     def no_of_seats(self):
#         pass
#     def break_type(self):  # Concrete method
#         print('Normal Break')
# class Suzuki(Car):
#     def no_of_seats(self,seats):
#         print(f'Number of seats is {seats}')
# class Toyata(Car):
#     def no_of_seats(self,seats):
#         print(f'Number of seats is {seats}')
#     def break_type(self):
#         print('Special Break')
# class Audi(Car):
#     def no_of_seats(self,seats):
#         print(f'Number of seats is {seats}')
#     def break_type(self):
#         print('Special as well as Powerful Break')
# s=Suzuki()
# s.no_of_seats(6)
# s.break_type()
# t=Toyata()
# t.no_of_seats(5)
# t.break_type()
# a=Audi()
# a.no_of_seats(4)
# a.break_type()