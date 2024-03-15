# Accessing Static Variable in different places

# 1.Outside of the class
# class Student:
#     college='NIT clg'
# print(Student.college)

# 2.Inside Constructor
# class Student:
#     college='NIT clg'
#     def __init__(self):
#         print(Student.college)
# s1=Student()

# 3.Inside Instance method
# class Student:
#     college='NIT clg'
#     def display(self):
#         print(Student.college)
# s1=Student()
# s1.display()

# 4.Inside class method
# class Student:
#     college='NIT clg'
#     @classmethod
#     def cm(cls):
#         print(Student.college)  # using class name
#         print(cls.college)  # using cls variable
# Student.cm()

# 5.Inside Static method
# class Student:
#     college='NIT clg'
#     @staticmethod
#     def sm():
#         print(Student.college)
# s1=Student()
# s1.sm()


# -----------------------------------------------------------------


# Modification of Static variable at different places

# 1.outside of the class
# class Employee:
#     company='Tech Mahindra'
# print(Employee.company)
# Employee.company='Imfosys'
# print(Employee.company)

# 2.Inside Constructor
# class Employee:
#     company='Tech Mahindra'
#     def __init__(self):
#         Employee.company='Imfosys'
# print(Employee.company)
# e1=Employee()
# print(Employee.company)

# 3.Inside Instance method
# class Employee:
#     company='Tech Mahindra'
#     def modify(self):
#         Employee.company='Imphosys'
# print(Employee.company)
# e1=Employee()
# e1.modify()
# print(Employee.company)

# 4.Inside Class method
# class Employee:
#     company='Tech Mahindra'
#     @classmethod
#     def cm(cls):
#         Employee.company='Imphosys'  # using class name
#         # cls.company='Microsoft'  # using cls variable
# print(Employee.company)
# e1=Employee()
# e1.cm()
# print(Employee.company)

# 5.Inside Static method
# class Employee:
#     company='Tech Mahindra'
#     @staticmethod
#     def sm():
#         Employee.company='Imphosys'
# print(Employee.company)
# e1=Employee()
# e1.sm()
# print(Employee.company)

# modifying Static variable using self(Unexpected Result)
# class Employee:
#     company='Tech Mahindra'
#     def __init__(self):
#         self.company='Imphosys'  # it will create an Instance variable instead of modifyig the Static variable
# print(Employee.company)
# e1=Employee()
# print(Employee.company)

# modifying Static variable using reference variable(Unexpected Result)
# class Employee:
#     company='Tech Mahindra'
# print(Employee.company)
# e1=Employee()
# e1.company='Imphosys'  # it will create an Instance variable for 'e1' object
# print(Employee.company)
# print(e1.__dict__)
# print(Employee.__dict__)


# ------------------------------------------------------


# Deletion of Static variable at different places

# 1.Outside of the class
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
# print(Student.__dict__)
# del Student.principal
# print('\n After Deletion \n')
# print(Student.__dict__)

# 2.Inside Constructor
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     def __init__(self):
#         del Student.college
# print(Student.__dict__)
# print('\n After Deletion \n')
# s1=Student()
# print(Student.__dict__)

# 3.Inside Instance method
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     def delete(self):
#         del Student.college
# print(Student.__dict__)
# print('\n After Deletion \n')
# s1=Student()
# s1.delete()
# print(Student.__dict__)

# 4.Inside Class Method
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     @classmethod
#     def cm(cls):
#         del Student.principal  # using class name
#         del cls.college  # using cls variable
# print(Student.__dict__)
# print('\n After Deletion \n')
# Student.cm()
# print(Student.__dict__)

# Inside Static method
# class Student:
#     college='NIT clg'
#     principal='Dr. Chand'
#     @staticmethod
#     def sm():
#         del Student.principal
# print(Student.__dict__)
# print('\n After Deletion \n')
# s1=Student()
# s1.sm()
# print(Student.__dict__)