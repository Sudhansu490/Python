# Without using MultiThread(Single Thread)
# class Test:
#     def fun1(self):
#         for i in range(5):
#             print('sonu')
#     def fun2(self):
#         for i in range(5):
#             print('prangya')
# obj=Test()
# obj.fun1()
# obj.fun2()
# It executes sequentially as only MainThread executing the whole program.

# ------------------------------------------------------------------------
# with MultiThreading
from threading import *

# 1.Creation of Thread in Functional Approach

# Ex=1
# def fun1():
#     for i in range(5):
#         print('sonu')
# def fun2():
#     for i in range(5):
#         print('Ananya')
# t1=Thread(target=fun1)
# t1.start()
# t2=Thread(target=fun2)
# t2.start()

# Ex=2(Thread Information)
# print('Line 34-:',current_thread().name)
# def fun1():
#     print('Line 36-:',current_thread().name)
#     for i in range(5):
#         print('sonu')
# def fun2():
#     print('Line 40-:',current_thread().name)
#     for i in range(5):
#         print('saina')
# print('Line 43-:',current_thread().name)
# t1=Thread(target=fun1)  # creation of Thread
# print('Line 45-:',current_thread().name)
# t1.start()
# print('Line 47-:',current_thread().name)
# t2=Thread(target=fun2)
# print('Line 49-:',current_thread().name)
# t2.start()
# print('Line 51-:',current_thread().name)

# Ex=4(pass argument)
# def fun1(name):
#     for i in range(5):
#         print(name)
# def fun2(name):
#     for j in range(5):
#         print(name)
# def fun3(name):
#     for k in range(5):
#         print(name)
# t1=Thread(target=fun1,args=('sonu',))
# t1.start()
# t2=Thread(target=fun2,args=('lipshika',))
# t2.start()
# fun3('ananya')

# Ex=5
# def fun1(name,addr):
#     for i in range(3):
#         print(f'Name-: {name}, Address-: {addr}')
# def fun2(name,addr):
#     for j in range(3):
#         print(f'Name-: {name}, Address-: {addr}')
# t1=Thread(target=fun1,kwargs={'name':'sonu','addr':'BBSR'})
# t1.start()
# fun2('Puja','Cuttack')

# -------------------------------------------------------------
# 2.Creation of Thread in an Object Oriented Approach

# Ex=1
# class Test:
#     def m1(self):
#         for i in range(3):
#             print('kappa')
#     def m2(self):
#         for j in range(3):
#             print('swastika')
# obj=Test()
# t1=Thread(target=obj.m1)
# t1.start()
# t2=Thread(target=obj.m2)
# t2.start()

# Ex=2(passing arguments)
# class Test:
#     def m1(self,name):
#         for i in range(3):
#             print(name)
#     def m2(self,name):
#         for j in range(3):
#             print(name)
# obj=Test()
# t1=Thread(target=obj.m1,args=('kappa',))
# t1.start()
# t2=Thread(target=obj.m2,args=('Soma',))
# t2.start()

# ----------------------------------------------
# 3.Creation of Thread by extending Thread class

# Ex=1
# class Test1(Thread):  # Extended from Thread class
#     def run(self):  # override run() method
#         for i in range(3):
#             print('Kappa')
# class Test2(Thread):  # Extended from Thread class
#     def run(self):  # override run() method
#         for j in range(3):
#             print('Lisa')
# obj1=Test1()
# obj1.start()
# obj2=Test2()
# obj2.start()

# Ex=2(using constructor & by passing arguments)
# class Test1(Thread):
#     def __init__(self,name):
#         Thread.__init__(self)
#         self.name=name
#     def run(self):
#         for i in range(3):
#             print(self.name)
# class Test2(Thread):
#     def __init__(self,name):
#         Thread.__init__(self)
#         self.name=name
#     def run(self):
#         for j in range(3):
#             print(self.name)
# obj1=Test1('sonu')
# obj1.start()
# obj2=Test2('Disha')
# obj2.start()
# NOTE-: If a subclass overrides the constructor, it must make sure to invoke the base class constructor(Thread.__init__(self)) before doing anything else to the thread.