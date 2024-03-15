# Method Overriding
# Whatever methods parent contain by default those methods are available to child class.If child class want,then child class can provide own implementation for those method,this mechanism is called Method Overriding.

# class P:
#     def fav_songs(self):
#         print('I Like Old Songs.')
# class C(P):
#     def fav_songs(self):
#         print('I Like New Songs')
# c=C()
# c.fav_songs()

# using super() function we can override the method.
# class P:
#     def bike(self):
#         print('I Like Yamha RX100.')
#     def phone(self):
#         print('I Like Keypard Phones.')
# class C(P):
#     def phone(self):
#         super().bike()
#         print('I Like Smart Phones.')
# c=C()
# c.phone()

# -------------------------------------------------------------------------------------

# Constructor Overriding
# Parent class constructor by default available to child class,if child class want then child class can override it.

# class P:
#     def __init__(self):
#         print('I Like Old Songs.')
# class C(P):
#     def __init__(self):
#         print('I Like New Songs.')
# c=C()

# using super() function we can override the constructor.
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