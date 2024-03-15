# Whenever we are executing our python program then immediately PVM will send request OS to create one thread and that is mainthread.
# If we want to work with Thread in python then we must import one inbuild module that is 'threading'.
# import threading
# print(1)
# print(2)
# print(3)
# print(threading.current_thread())  # <_MainThread(MainThread, started 9324)>
# for i in range(5):
#     print('sonu')
# print(threading.current_thread())  # <_MainThread(MainThread, started 9324)>
# print(threading.current_thread().getName())  # Thread Name(MainThread)
# print(threading.current_thread().name)  # Thread Name(MainThread) 
# print(threading.current_thread().ident)  # Thread ID(9324)
# print(threading.current_thread().is_alive())  # active or not