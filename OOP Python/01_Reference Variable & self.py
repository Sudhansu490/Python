# create a class(Student) having properties are name,age & course.

# class Student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def printDetails(self):
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Course is {self.course}')
# s1=Student('Rohit',25,'MBA')
# s1.printDetails()
# s2=Student('Mohit',24,'MCA')
# s2.printDetails()

# --------------------------------------------------------------------------------------

# create a class(Employee) having properties are name,age & address by taking user inputs.

# class Employee:
#     def __init__(self):
#         self.name=input('Enter Your Name: ')
#         self.age=int(input('Enter the Age: '))
#         self.address=input('Enter the Address: ')
#     def printDetails(self):
#         print('-'*30)
#         print(f'Name is {self.name}')
#         print(f'Age is {self.age}')
#         print(f'Address is {self.address}')
# e1=Employee()
# e2=Employee()
# e3=Employee()
# e1.printDetails()
# e2.printDetails()
# e3.printDetails()

# --------------------------------------------------------------

# self & reference variable always points a same memory location
# class Student:
#     def __init__(self):
#         print(id(self))
# s1=Student()
# print(id(s1))
# print('-'*10)
# s2=Student()
# print(id(s2))

# --------------------------------------------------------------

# self is not a keyword, we can take any name in place of self.

# class Student:
#     def __init__(X):
#         X.name=input('Enter Your Name: ')
#         X.age=int(input('Enter the Age: '))
#         X.course=input('Enter the Course: ')
#     def printDetails(X):
#         print(f'Name is {X.name}')
#         print(f'Age is {X.age}')
#         print(f'Course is {X.course}')
# s1=Student()
# s1.printDetails()

# ---------------------------------------

# here 'name' is acting as self variable.

# class Employee:
#     def __init__(name,age,eid):
#         name.age=age
#         name.eid=eid
#     def printDetails(name):
#         print(f'Age of Employee is {name.age}')
#         print(f'Employee ID is {name.eid}')
# e1=Employee(25,2001297198)
# e1.printDetails()