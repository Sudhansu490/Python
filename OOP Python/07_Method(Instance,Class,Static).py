# Instance Method

# The first argument of Instance method is 'self'.Inside the class we can call Instance method by using self variable & outside the class we can call through object reference.
# class Calculation:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         result= self.a + self.b
#         print(f'Addition is {result}')
# c1=Calculation(10,5)
# c1.add()

# We can call one Instance method inside another Instance Method.
# class Calculation:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         result=self.a+self.b
#         print(f'Addition is {result}')
#         self.sub()
#     def sub(self):
#         result=self.a-self.b
#         print(f'Subtraction is {result}')
# c1=Calculation(10,20)
# c1.add()

# By using Instance Method we can perform various operations like modify,delete etc.
# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def update(self,m,n):
#         self.a=m
#         self.b=n
#     def delete(self):
#         del self.a
# t1=Test(25,50)
# print(t1.__dict__)
# t1.update(20,30)
# print(t1.__dict__)
# t1.delete()
# print(t1.__dict__)

# -------------------------------

# Class Method

# @classmethod decorator we have to write before class method.First argument of the class method is cls.
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     @classmethod
#     def cm(cls):
#         print(f'College Name is {Student.college}')
#         print(f'Principal Name is {cls.principal}')
# Student.cm()  # call class method using class name
# s1=Student()

# We can call one class method inside another class method by using class name or cls variable.By using class method we can perform various operations like modify,delete etc.
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     @classmethod
#     def cm(cls):
#         print(f'College Name is {Student.college}')
#     @classmethod
#     def modify(cls):
#         cls.college='GIFT clg'
#         cls.delete()  # using cls variable
#         # Student.delete()  # using class name
#     @classmethod
#     def delete(cls):
#         del cls.principal
# Student.cm()
# print(Student.__dict__)
# Student.modify()
# Student.cm()
# print(Student.__dict__)

# -------------------------------------------------

# Static Method

# Inside Static method we can use only local variables.No argument is required for Static method.We can call one static method inside another static method.
# calling Static method inside & outside of the class
# class Calculation:
#     @staticmethod
#     def add(a,b):
#         print(f'Addition is {a+b}')
#         Calculation.sub(25,15)  # using class name
#     @staticmethod
#     def sub(a,b):
#         print(f'Subtraction is {a-b}')
# Calculation.add(20,10)  # using class name
# c1=Calculation()
# c1.add(30,70)  # using reference variable