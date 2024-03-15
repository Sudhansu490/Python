# Static Variable(Class Level Variable)
#---------------------------------------------

# Creation of Static Variable at different places

# 1.Inside class directly(Outside of constructor & Instance Method)
# class Student:
#     college='NIT College'  # static variable
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
# s1=Student('Rahul',25)
# print(s1.__dict__)  # {'name': 'Rahul', 'age': 25}
# print(Student.__dict__)

# ---------------------------------------------------

# 2.Outside of class(using class name)
# class Student:
#     pass
# s1=Student()
# Student.college='NIT College'
# Student.branch='CSE'
# print(s1.__dict__)  # {}
# print(Student.__dict__)

# ---------------------------------------------

# 3.Inside Constructor(using class name)
# class Student:
#     def __init__(self,name):
#         self.name=name
#         Student.college='NIT clg'
# s1=Student('Rohit')
# print(Student.__dict__)

# --------------------------------------------

# 4.Inside Instance Method(using class name)
# class Student:
#     def create(self,name):
#         Student.college='NIT clg'
#         self.name=name
# s1=Student()
# s1.create('Rahul')  # As this is method so at the time of calling method we can pass the 'name'
# print(s1.__dict__)
# print(Student.__dict__)

# ----------------------------------------------------------------------

# 5.Inside class method

# using class name
# class Student:
#     @classmethod  # Decorator
#     def cm(cls):  # first argument of class method is always 'cls'
#         Student.college='NIT clg'
# s1=Student()
# Student.cm()
# print(Student.__dict__)

# using 'cls' variable
# class Student:
#     @ classmethod
#     def cm(cls,name):
#         cls.college='NIT clg'  # Always 'cls' points to current class object
#         cls.name=name
#         print(id(cls))
# s1=Student()
# s1.cm('Rohit')
# print(s1.__dict__)  # {}(As name & college is class level variable)
# print(Student.__dict__)
# print(id(Student))  
# Both cls & Student are pointing to same memory location 

# --------------------------------------------------------------------

# 6.Inside static method
# class Student:
#     @staticmethod
#     def sm():  # For static method creation, no argument is needed
#         Student.college='NIT clg'
# s1=Student()
# s1.sm()
# print(Student.__dict__)