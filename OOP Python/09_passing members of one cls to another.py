# passing members of one class to another class

# class Student:
#     def __init__(self,name,age,roll,address):
#         self.name=name
#         self.age=age
#         self.roll=roll
#         self.address=address
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Roll No is {self.roll}')
#         print(f'Address is {self.address}')
# class Normal:
#     @staticmethod
#     def modify(r):
#         r.address='Cuttack'
# s1=Student('Sonu',25,2001297198,'BBSR')
# s1.printDetails()
# print('-'*25)
# Normal.modify(s1)
# s1.printDetails()

# class A:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def printDetails(self):
#         print(f'X is {self.x}')
#         print(f'Y is {self.y}')
# class B:
#     @staticmethod
#     def modify(r):
#         r.y=999
# a1=A(100,200)
# a1.printDetails()
# print('-'*10)
# B.modify(a1)
# a1.printDetails()

# passing single member of a class to another class
# class Student:
#     def __init__(self,name,age,roll,address):
#         self.name=name
#         self.age=age
#         self.roll=roll
#         self.address=address
# class Normal:
#     @staticmethod
#     def printInfo(r):
#         print(r)
# s1=Student('Rohit',25,1024,'BBSR')
# Normal.printInfo(s1.age)
# Normal.printInfo(s1.address)