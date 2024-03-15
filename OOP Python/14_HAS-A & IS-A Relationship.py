# HAS-A Relationship(Composition/Containership/Complex objects)

# class Car:
#     def __init__(self,cbrand,ccolor,cprice):
#         self.cbrand=cbrand
#         self.ccolor=ccolor
#         self.cprice=cprice
#     def printCarDetails(self):
#         print('-'*30)
#         print(f'Car Brand is {self.cbrand}')
#         print(f'Car Colour is {self.ccolor}')
#         print(f'Car Price is {self.cprice}')
# class Laptop:
#     def __init__(self,lbrand,lcolor,lprice):
#         self.lbrand=lbrand
#         self.lcolor=lcolor
#         self.lprice=lprice
#     def printLaptopDetails(self):
#         print('-'*30)
#         print(f'Laptop Brand is {self.lbrand}')
#         print(f'Laptop Colour is {self.lcolor}')
#         print(f'Laptop Price is {self.lprice}')
# class Employee:
#     def __init__(self,ename,eid,eaddress):
#         self.ename=ename
#         self.eid=eid
#         self.eaddress=eaddress
#         self.c=Car('Thar','Black',100000)  # object creation of 'car' class
#         self.l=Laptop('Dell','Silver',45000)  # object creation of 'Laptop' class
#     def printEmpDetails(self):
#         print(f'Employee Name is {self.ename}')
#         print(f'Employee ID is {self.eid}')
#         print(f'Employee Address is {self.eaddress}')
#         self.c.printCarDetails()
#         self.l.printLaptopDetails()
# e1=Employee('Sujit',1024,'BBSR')
# e1.printEmpDetails()
# NOTE- Without existence of container object there is no existence of contained object.
# Here class Employee is container object but class Car & class Laptop is contained object.If Employee object is not existed then there is no chance of existence of Car & Laptop object.

# In HAS-A Relationship we will build object from smaller objects.
# class Department:
#     def __init__(self,dname,did):
#         self.dname=dname
#         self.did=did
#     def printDeptDetails(self):
#         print('-'*27)
#         print(f'Department Name is {self.dname}')
#         print(f'Department ID is {self.did}')
# class University:
#     def __init__(self,uname,uaddress):
#         self.uname=uname
#         self.uaddress=uaddress
#         self.d=Department('CSE',1024)  
#         self.d1=Department('ME',2024)
#         self.d2=Department('EE',3024)
#         self.d3=Department('AI/ML',4024)
#     def printUniverDetails(self):
#         print(f'University Name is {self.uname}')
#         print(f'University Address is {self.uaddress}')
#         self.d.printDeptDetails()
#         self.d1.printDeptDetails()
#         self.d2.printDeptDetails()
#         self.d3.printDeptDetails()
# u=University('NIT','BBSR')
# u.printUniverDetails()

# -----------------------------------------------------------

# IS-A Relationship(Inheritance)

# class A:  # Old/Base/Parent Class
#     def method1(self):
#         print('A Class Method 1')
#     def method2(self):
#         print('A Class Method 2')
#     def method3(self):
#         print('A Class Method 3')
# class B(A):  # New/Derived/Child
#     def method4(self):
#         print('B Class Method 4')
# b=B()
# b.method4()
# b.method1()
# b.method2()
# b.method3()

# If we will create a New Class from an Old Class then we can access all the members of the Old Class inside the New Class.
# class A:
#     def __init__(self):
#         self.x=10
#         self.y=20
# class B(A):
#     def printDetails(self):
#         print(f'X value is {self.x}')
#         print(f'Y value is {self.y}')
# b=B()
# b.printDetails()