# Local Variable(Temporary Variable)
# ---------------------------------------

# Local Variable creates inside a method.
# class Calculation:
#     def add(self):
#         a=15  # Local Variable
#         b=17
#         result=a+b
#         print(result)
# c1=Calculation()
# c1.add()

# At the time of method execution local variables are created & once method execution is completed it will destroyed from memory
# class Calculation:
#     def test(self):
#         a=100
#         b=200
#         print(a)
#         print(b)
#     def demo(self):
#         print(a)  # NameError
#         print(b)  # NameError
# c1=Calculation()
# c1.test()
# c1.demo()

# We can access local variables inside the method,we can't access them outside of the method
# class Student:
#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll
#     def printDetails(self):
#         print(self.name)  # accessing Instance Variable
#         print(name)  # accessing Local Variable(NameError)
# s1=Student('Rohit',25,1024)
# s1.printDetails()