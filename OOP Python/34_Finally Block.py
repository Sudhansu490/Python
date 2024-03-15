# Inside finally block we will write clean-up code(must executed codes)
# Finally, is a block and it will execute every time, it doesnot matter whether exception raised or not, exception handle or not.

# Ex=1
# try:
#     print('File opening code.')
# except Exception as e:
#     print(e)
# finally:
#     print('File closing code.')

# Ex=2
# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print(z)
# finally:
#     print('Finally block executed.')

# Ex=3
# try:
#     print(10/0)
# except FileNotFoundError as f:
#     print(f)
# finally:
#     print('Finally block executed.')

# Ex=4(Always write the clean-up codes in finally bock)
# try:
#     print('1')
#     print('2')
#     print('3')
#     print('File-1 opening code')
#     print('File-2 opening code')
#     print('4')
#     print('5') 
#     print(10/0)
# except Exception as e:
#     print(e)
# finally:
#     print('File-1 closing code')  
#     print('File-2 closing code')
#     print('Finally block executed.')

# -----------------------------------------------------------

# Is there any situation where Finally block won't be execute

# 1.If we will forcefully shut down PVM(Python Virtual Machine)
# import os
# try:
#     print('1')
#     print('2')
#     os._exit(0)  # this is the code to shut down PVM
#     print(3)
# except Exception as e:
#     print(e)
# finally:
#     print('Finally block executed.')

# 2.Inside function if we will write finally block after return statement(wrong)
# def fun():
#     try:
#         print('1')
#         return 'hello'
#         print('2')
#     except Exception as e:
#         print(e)
#     finally:
#         print('Finally block executed.') 
# print(fun())