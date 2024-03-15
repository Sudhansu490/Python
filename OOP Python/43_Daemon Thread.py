# 1.Daemon Threads are running continously in memory.
# 2.Garbage collector is the best example of Daemon Thread.
# 3.Garbage collector is used to delete useless objects from the memory at the time of program execution.
# 4.MainThread is always Non-Daemon and we can't change it as daemon Thread.
# 5.By using Daemon property, we can set a Thread as Daemon Thread also by using this property we can check the Thread is Daemon or not.
# 6.Once a Thread is started we can't change its nature.

from threading import *
import time

# Ex=1
# print('MainThread is Daemon-:',current_thread().daemon)  # False

# Ex=2
# def fun():
#     for i in range(3):
#         print('kappa')
#         time.sleep(1)
# t1=Thread(target=fun)
# print('t1 Thread is Daemon-:',current_thread().daemon)  # False
# t1.start()

# Ex=3(set t1 Thread as Daemon)
# def fun():
#     for i in range(3):
#         print(i)
#         time.sleep(1)
# t1=Thread(target=fun,daemon=True)
# print('t1 Thread is Daemon-:',t1.daemon)
# t1.start()
# print('End of MainThread execution.')
# NOTE-:Once MainThread completes its execution, then remaining all the Threads will destroy from the memory.

# Ex=4
# def fun():
#     for i in range(5):
#         print(i)
#         time.sleep(1)
# t1=Thread(target=fun,daemon=True)
# print('t1 Thread is daemon-:',t1.daemon)
# t1.start()
# time.sleep(2)
# print('End of MainThread execution.')

# Ex=5
# def fun1():
#     for i in range(4):
#         print('Hi')
#         time.sleep(1)
#     t2=Thread(target=fun2)
#     t2.start()
# def fun2():
#     for i in range(4):
#         print('Hello')
#         time.sleep(1)
# t1=Thread(target=fun1,daemon=True)
# print('t1 Thread is Daemon-:',t1.daemon)
# t1.start()
# time.sleep(6)
# print('End of MainThread execution.')

# Ex=6(ask name to the user & check how much time user taken to give his/her name)
# def time_count():
#     sec=0
#     while True:
#         time.sleep(1)
#         sec=sec+1
#         print(f'I am waiting since {sec} Seconds')
# t1=Thread(target=time_count,daemon=True)
# t1.start()
# name=input('Enter Your Name: \n')

# Ex=7
# def fun():
#     for i in range(5):
#         print('Hello')
#         time.sleep(1)
# t1=Thread(target=fun)
# t1.start()
# t1.daemon=True  # t1 Thread is already started now i try to change its nature
# NOTE-: RuntimeError: cannot set daemon status of active thread

# Ex=8
# current_thread().daemon=True  # RuntimeError: cannot set daemon status of active thread