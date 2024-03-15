# Instance Variable(Object Level Variable)
#--------------------------------------------------

# Creation of Instance Variable

# 1.create Instance variable inside class inside constructor.
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
# s1=Student('Kappa',20,2001297198)
# print(s1.__dict__)

# 2.create Instance Variable inside class inside Instance method.
# class Student:
#     def create(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
# s1=Student()
# print(s1.__dict__)
# s1.create('Sonu',25,2001297200)
# print(s1.__dict__)

# 3.create Instance Variable outside class using object reference.
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student('Lalit',27)
# print(s1.__dict__)
# s1.roll=2121297500
# print(s1.__dict__)

# --------------------------------------------------

# Accessing Instance Variable from different places.

# 1.access Instance variable inside class inside constructor.
# class Employee:
#     def __init__(self,name,age,eid):
#         self.name=name
#         self.age=age
#         self.eid=eid
#         print(f'Employee Name is {self.name}')
#         print(f'Employee Age is {self.age}')
#         print(f'Employee ID is {self.eid}')
# e1=Employee('Kunal',24,1024)

# 2.access Instance variable inside class inside Instance method.
# class Employee:
#     def __init__(self,name,age,eid):
#         self.name=name
#         self.age=age
#         self.eid=eid
#     def printDetails(self):
#         print(f'Employee Name is {self.name}')
#         print(f'Employee Age is {self.age}')
#         print(f'Employee ID is {self.eid}')
# e1=Employee('Shibu',26,2024)
# e1.printDetails()

# 3.access Instance variable outside the class using object reference
# class Employee:
#     def __init__(self,name,age,eid):
#         self.name=name
#         self.age=age
#         self.eid=eid
# e1=Employee('Mohan',28,3024)
# print(f'Employee Name is {e1.name}')
# print(f'Employee Age is {e1.age}')
# print(f'Employee ID is {e1.eid}')

# ---------------------------------------------------------------

# Deletion of Instance variable from different places.

# 1.delete Instance variable from inside class inside constructor.
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
#         print(self.__dict__)
#         del self.age
#         print(self.__dict__)
# s1=Student('Pushkar',26,2001297100)

# 2.delete Instance variable from inside class inside Instance method.
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
#     def deleteData(self):
#         del self.roll
# s1=Student('Susan',24,2001297450)
# print(s1.__dict__)
# s1.deleteData()
# print(s1.__dict__)

# 3.delete Instance variable from outside class using object reference variable.
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
# s1=Student('Jishu',29,2001297550)
# print(s1.__dict__)
# del s1.age,s1.roll
# print(s1.__dict__)