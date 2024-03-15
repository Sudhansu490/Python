# 1.Constructor is a special method as it will execute automatically at the time of object creation.
# 2.Constructor is used to assigning values to the Instance variable.
# 3.In Python __init__(self) method acts as constructor.
# 4.Constructor will only once per object.
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Roll No is {self.roll}')
# s1=Student('Rohit',25,1024)
# s1.printDetails()
# s1.printDetails()

# 5.Define a class without constructor
# class Employee:
#     def companyName(self):
#         print('Company Name is TCS pvt. Ltd.')
# e1=Employee()
# e1.companyName()

# 6.If we will call the Constructor manually then Python will treated as a normal method call.
# class Demo:
#     def __init__(self):
#         print('It is a Demo Class.')
# d=Demo()  # Constructor will execute automatically.
# d.__init__()  # Python will treat __init__(self) as a normal method.
# d.__init__()

# 7.We can't create multiple constructors inside a class bcoz method overloading is not possible in python,but if we will create multiple constructors inside a class thrn it will treated last one & it will not raise any error.
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
# s=Student('Mohit',23)
# s.printDetails()

# -----------------------------------------

# Types of Constructor

# Non-Parameterize Constructor
# class Demo1:
#     def __init__(self):
#         print('I am Non-Parameterize Constructor.')
# d1=Demo1()

# Parameterize Constructor
# class Demo2:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print('I am Parameterize Constructor.')
# d2=Demo2('Kunal',25)

# Default Constructor
# class Demo3:
#     def type3(self):
#         print('I am Default Constructor.')
# d3=Demo3()
# d3.type3()  # Here python will treat the method as __init__(self) constructor.