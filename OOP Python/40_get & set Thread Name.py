from threading import *

# How to get Thread Name
# class Test:
#     print('Line 5-:',current_thread().name)  # MainThread
#     def fun1(self):
#         print('Line 7-:',current_thread().name)  # Thread-1 (fun1)
#         for i in range(5):
#             print('sonu')
#     def fun2(self):
#         print('Line 11-:',current_thread().name)  # Thread-2 (fun2)
#         for j in range(5):
#             print('sona')
# obj=Test()
# print('Line 15-:',current_thread().name)  # MainThread
# t1=Thread(target=obj.fun1)
# t1.start()
# print('Line 18-:',current_thread().name)  # MainThread
# t2=Thread(target=obj.fun2)
# t2.start()
# print('Line 21-:',current_thread().name)  # MainThread

# ------------------------------------------------------
# How to set Thread Name

# Approach 1
# class Test:
#     def fun1(self):
#         for i in range(3):
#             print('kappa')
#     def fun2(self):
#         for j in range(3):
#             print('pipili')
# obj=Test()
# t1=Thread(target=obj.fun1,name='myThread1')  # set Thread Name
# t1.start()
# print(t1.name)  # myThread1
# t2=Thread(target=obj.fun2,name='myThread2')  # set Thread name
# t2.start()
# print(t2.name)  # myThread2

# Approach 2
# class Test1(Thread):
#     def run(self):
#         print(current_thread().name)  # myThread1
#         for i in range(5):
#             print('kappa')
# class Test2(Thread):
#     def run(self):
#         print(current_thread().name)  # myThread2
#         for i in range(5):
#             print('rajlaxmi')
# ob1=Test1()
# ob1.name='myThread1'  # set Thread Name
# ob1.start()
# ob2=Test2()
# ob2.name='myThread2'  # set Thread Name
# ob2.start()