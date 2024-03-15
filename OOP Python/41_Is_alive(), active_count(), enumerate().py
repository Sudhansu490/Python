# sleep()
import time

# Ex=1
# for i in range(5):
#     print(i)
#     time.sleep(5)

# Ex=2
# print('Kappa')
# time.sleep(2)
# print('Bijayini')
# time.sleep(3)
# print('Elina')

# ------------------------------------------------------------------------------------------------------------------
# Is_alive() method
# This method is used to check whether that the Thread is alive or not that means the Thread is still running or not.
# If it is running then it will return True or else False.
# from threading import *

# Ex=1
# def fun1():
#     print('sonu')
#     time.sleep(5)
#     print('saina')
# t1=Thread(target=fun1)
# print('Before starting t1 Thread-:',t1.is_alive())
# t1.start()
# print('After starting t1 Thread-:',t1.is_alive())

# Ex=2
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     print('swastika')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# print('Before starting t1 Thread-:',t1.is_alive())
# print('Before starting t2 Thread-:',t2.is_alive())
# t1.start()
# t2.start()
# print('After starting t1 Thread-:',t1.is_alive())
# print('After starting t2 Thread-:',t2.is_alive())

# Ex=3
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     time.sleep(10)
#     print('champa')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# print('Before starting t1 Thread-:',t1.is_alive())
# print('Before starting t2 Thread-:',t2.is_alive())
# t1.start()
# t2.start()
# print('After starting t1 Thread-:',t1.is_alive())
# print('After starting t2 Thread-:',t2.is_alive())

# Ex=4
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     time.sleep(10)
#     print('champa')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# print('Before starting t1 Thread-:',t1.is_alive())
# print('Before starting t2 Thread-:',t2.is_alive())
# t1.start()
# t2.start()
# time.sleep(15)
# print('After starting t1 Thread-:',t1.is_alive())
# print('After starting t2 Thread-:',t2.is_alive())

# Ex=5
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     time.sleep(5)
#     print('champa')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# print('Before starting t1 Thread-:',t1.is_alive())
# print('Before starting t2 Thread-:',t2.is_alive())
# t1.start()
# t2.start()
# time.sleep(5)
# print('After starting t1 Thread-:',t1.is_alive())
# print('After starting t2 Thread-:',t2.is_alive())

# -------------------------------------------------
# active_count() method
# It is used to count the number of active Threads.
# from threading import *

# Ex=1(Only MainThread is active)
# def fun1():
#     print('kappa')
# def fun2():
#     print('Narmada')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# print('Number of Active Thread-:',active_count())
# t1.start()
# t2.start()

# Ex=2
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     print('Swagatika')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# time.sleep(3)
# print('Number of Active Thread-:',active_count())

# Ex=3
# def fun1():
#     print('start-:fun1')
#     time.sleep(2)
#     print('stop-:fun1')
# def fun2():
#     print('start-:fun2')
#     time.sleep(2)
#     print('stop-:fun2')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# print('Number of Active Thread-:',active_count())
# time.sleep(5)
# print('Number of Active Thread-:',active_count())

# Ex=4
# def fun1():
#     print('start-:fun1')
#     time.sleep(2)
#     print('stop-:fun1')
# def fun2():
#     print('start-:fun2')
#     time.sleep(2)
#     print('stop-:fun2')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# print('Number of Active Thread-:',active_count())
# time.sleep(2)
# print('Number of Active Thread-:',active_count())

# -------------------------------------------------
# enumerate() function
# It returns a list of all active thread objects.
from threading import *

# Ex=1
# print(enumerate())

# Ex=2
# def fun():
#     time.sleep(5)
#     print('kappa')
# t1=Thread(target=fun)
# t1.start()
# print(enumerate())

# Ex=3
# def fun1():
#     time.sleep(5)
#     print('kappa')
# def fun2():
#     print('Swagatika')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# time.sleep(3)
# print(enumerate())

# Ex=4
# def fun1():
#     print('start-:fun1')
#     time.sleep(2)
#     print('stop-:fun1')
# def fun2():
#     print('start-:fun2')
#     time.sleep(2)
#     print('stop-:fun2')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# print(enumerate())
# time.sleep(5)
# print(enumerate())

# Ex=5
# def fun1():
#     print('start-:fun1')
#     time.sleep(2)
#     print('stop-:fun1')
# def fun2():
#     print('start-:fun2')
#     time.sleep(2)
#     print('stop-:fun2')
# t1=Thread(target=fun1)
# t2=Thread(target=fun2)
# t1.start()
# t2.start()
# print(enumerate())
# time.sleep(2)
# print(enumerate())