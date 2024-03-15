# If Parent class & Child class having members with same name then from Child class we can access Parent class members using Super() function.
# Super() function is used to access Parent class members.
# Super() function contains the history of Super class method, that's why we can say Super() is used to refer Super class members.

# problems without Super() function
# class Employee:
#     def __init__(self,name,age,eid,sal):
#         self.name=name
#         self.age=age
#         self.eid=eid
#         self.sal=sal
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Employee ID is {self.eid}')
#         print(f'Salary is {self.sal}')
# class Student:
#     def __init__(self,name,age,sid,course,clg):
#         self.name=name
#         self.age=age
#         self.sid=sid
#         self.course=course
#         self.clg=clg
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Student ID is {self.sid}')
#         print(f'Course is {self.course}')
#         print(f'College is {self.clg}')
# class Faculty:
#     def __init__(self,name,age,fid,dept,clg):
#         self.name=name
#         self.age=age
#         self.fid=fid
#         self.dept=dept
#         self.clg=clg
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Faculty ID is {self.fid}')
#         print(f'Department is {self.dept}')
#         print(f'College is {self.clg}')
# e=Employee('Sunam',24,1024,25000)
# e.printDetails()
# print('-'*25)
# s=Student('Amit',25,2024,'MTech','NIT clg')
# s.printDetails()
# print('-'*25)
# f=Faculty('Rath',30,3024,'CSE','GIFT clg')
# f.printDetails()

# Solution by using Super() function
# class Human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
# class Employee(Human):
#     def __init__(self,name,age,eid,sal):
#         super().__init__(name,age)
#         self.eid=eid
#         self.sal=sal
#     def printDetails(self):
#         super().printDetails()
#         print(f'Employee ID is {self.eid}')
#         print(f'Salary is {self.sal}')
# class Student(Human):
#     def __init__(self,name,age,sid,course,clg):
#         super().__init__(name,age)
#         self.sid=sid
#         self.course=course
#         self.clg=clg
#     def printDetails(self):
#         super().printDetails()
#         print(f'Student ID is {self.sid}')
#         print(f'Course is {self.course}')
#         print(f'College is {self.clg}')
# class Faculty(Human):
#     def __init__(self,name,age,fid,dept,clg):
#         super().__init__(name,age)
#         self.fid=fid
#         self.dept=dept
#         self.clg=clg
#     def printDetails(self):
#         super().printDetails()
#         print(f'Faculty ID is {self.fid}')
#         print(f'Department is {self.dept}')
#         print(f'College is {self.clg}')
# e=Employee('Sunam',24,1024,25000)
# e.printDetails()
# print('-'*25)
# s=Student('Amit',25,2024,'MTech','NIT clg')
# s.printDetails()
# print('-'*25)
# f=Faculty('Rath',30,3024,'CSE','GIFT clg')
# f.printDetails()

# -----------------------------------------------------

# call methods of a particular class from child class

# Example 1
# class A:
#     def mt1(self):
#         print('A-mt1')
# class B(A):
#     def mt1(self):
#         print('B-mt1')
# class C(A):
#     def mt1(self):
#         print('C-mt1')
# class D(B,C):
#     def mt1(self):
#         print('D-mt1')
#         B.mt1(self)  # calling mt1() of B class
#         A.mt1(self)
# d=D()
# d.mt1()

# Example 2
# class A:
#     def mt1(self):
#         print('A-mt1')
# class B(A):
#     def mt1(self):
#         print('B-mt1')
# class C(A):
#     def mt1(self):
#         print('C-mt1')
#         super().mt1()  # priority of A class(Child of A class)
# class D(B,C):
#     def mt1(self):
#         print('D-mt1')
#         super().mt1()  # priority of B class
# c=C()
# c.mt1()
# d=D()
# d.mt1()