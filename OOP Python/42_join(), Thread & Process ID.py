# join() method
# Normally in multithreading, multiple Threads can execute simultaneously but there are some situation where a Thread wants to wait until completion of another Thread execution then we should go for join() method.
# from threading import *
# import time

# Ex=1
# def fun():
#     for i in range(3):
#         print('ChildThread')
# t1=Thread(target=fun)
# t1.start()
# t1.join()  # now onwards MainThread will wait until completion of t1 Thread execution 
# for i in range(3):
#     print('MainThread')

# Ex=2
# def fun1():
#     for i in range(3):
#         print('Ananya')
# def fun2():
#     t1.join()  # This Thread will execute after execution of t1 Thread.
#     for j in range(3):
#         print('Swastika')
# def fun3():
#     for k in range(3):
#         print('Prangya')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t3=Thread(target=fun3)
# t1.start()
# t2.start()
# t3.start()

# Ex=3
# def fun():
#     for i in range(4):
#         time.sleep(3)
#         print('Lipshika')
# t1=Thread(target=fun)
# t1.start()
# t1.join(5)  # MainThread will execute after 5 Seconds.
# for i in range(4):
#     print('Dikhita')

# Ex=4
# def fun():
#     for i in range(4):
#         time.sleep(3)
#         print('Bijayini')
# t1=Thread(target=fun)
# t1.start()
# t1.join(5)
# for i in range(4):
#     time.sleep(2)
#     print('Ankita')

# ------------------------------------------
# Process ID
# Program is on execution is called Process.
# Whenever we will execute a python program then Operating System will create a process, that has some unique number, this number is called Process ID.
# By using getpid() function we can get Process ID, which is available inside OS module.
# from threading import *
# import os

# def fun():
#     print('KAPPA')
# fun()
# print(os.getpid())

# ---------------------------------------------------------------------------
# Thread ID
# Every Thread have some unique ID number, this ID number is called Thread ID.
# Thread won't get ID number at the time of Thread object creation, once it started it gets the ID number.
# We can change Thread name but we can't change its ID.
# By using ident variable, we can get Thread ID.
# from threading import *

# def fun1():
#     print('Swastika')
# def fun2():
#     print('Prangya')

# t1=Thread(target=fun1)
# print('t1 Thread ID before starting-:',t1.ident)  # None
# t1.start()
# print('t1 Thread ID after starting-:',t1.ident)

# t2=Thread(target=fun2)
# print('t2 Thread ID before starting-:',t2.ident)  # None
# t2.start()
# print('t2 Thread ID after starting-:',t2.ident)