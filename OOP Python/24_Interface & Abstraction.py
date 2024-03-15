# Interface

# Interface is just like Abstract class, but Interface only contain Abstract method where as Abstract class contain Abstract as well as Concrete method.
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def no_of_seats(self):
#         pass
#     @abstractmethod
#     def no_of_whls(self):
#         pass
# # v=Vehicle()  # TypeError: Can't instantiate abstract class Vehicle with abstract methods
# class Bus(Vehicle):
#     def no_of_seats(self):
#         print('Number of seats in Bus 40+')
#     def no_of_whls(self):
#         print('Number of wheels in Bus 4')
#     def n1(self):
#         print('Normal Method n1')
# class Car(Vehicle):
#     def no_of_seats(self):
#         print('Number of seats in Car 4+')
#     def no_of_whls(self):
#         print('Number of wheels in Car 4')
#     def n2(self):
#         print('Normal Method n2')
# b=Bus()
# b.no_of_seats()
# b.no_of_whls()
# b.n1()
# print('-'*27)
# c=Car()
# c.no_of_seats()
# c.no_of_whls()
# c.n2()

# ----------------------------------------------------------------

# Abstraction

# Abstraction means hiding the implementation part & showing the functionality part to the user.
# By using Abstract class & Interface we can achieve Abstraction.
# By using Interface we can achieve 100% Abstraction whereas by using Abstract class we can achieve 0 to 100% Abstraction.