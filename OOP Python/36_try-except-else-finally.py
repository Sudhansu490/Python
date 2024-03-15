# Complete flow of execution of (try-except-else-finally block)

# Q.1=>WAP to open three files file2.txt,file4.txt & file1.txt. If any of these files are not present, a message without exiting the program must be printed prompting the same.
# def readFile(filename):
#     try:
#         with open(filename,'r') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print(f'File {filename} is not found.')
# readFile('OOP Python/file2.txt')
# readFile('OOP Python/file4.txt')
# readFile('OOP Python/file1.txt')

# Ex=1:
# try:
#     print('1')
#     print('2')
#     print(23+'sonu')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#     print('3')
# except e:  # NameError: name 'e' is not defined
#     print(e)
# finally:
#     print('end')

# Ex=2:
# try:
#     print('1')
#     print('2')
#     print(23+'sonu')
#     print('3')
# except :
#     try:
#         print(e)
#     except Exception as e:
#         print(e)  # name 'e' is not defined
# finally:
#     print('end')

# Ex=3
# try:
#     print(23+'sonu')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# except:
#     try:
#         print(e)  # NameError: name 'e' is not defined
#     except TypeError as t:
#         print(t)
# finally:
#     print('end')

# Ex=4
# try:
#     print(23+'sonu')
# except:
#     try:
#         print(e)
#     except TypeError as t:
#         print(t)
#     except Exception as e:
#         print(e)  # name 'e' is not defined
#     except NameError:
#         print('NameError occur')
# finally:
#     print('end')

# Ex=5
# try:
#     print(23+'sonu')
# except:
#     try:
#         print(e)
#     except Exception as e:
#         print(e)  # name 'e' is not defined
#     finally:
#         print('Inner finally block')
# finally:
#     print('Outer finally block')

# Ex=6
# try:
#     print(10/0)
# except Exception as e:
#     print(e)  # division by zero
#     print('sonu'+10)  # TypeError: can only concatenate str (not "int") to str
#     print('99')
# else:
#     print('I am else block')
# finally:
#     print('end')

# Ex=7
# try:
#     print(10/0)
# except Exception as e:
#     print(e)  # division by zero
#     try:
#         print(20+'sonu')
#     except Exception as e:
#         print(e)  # unsupported operand type(s) for +: 'int' and 'str'
#     print('99')
# else:
#     print('I am else block')
# finally:
#     print('end')

# Ex=8
# import os
# try:
#     print(10/0)
# except Exception as e:
#     print(e)  # division by zero
#     try:
#         print(10+'sonu')
#     except Exception as e:
#         print(e)  # unsupported operand type(s) for +: 'int' and 'str
#         os._exit(0)  # execution stopped
#     print('99')
# else:
#     print('I am else block')
# finally:
#     print('end')

# Ex=9
# try:
#     print('1')
#     print('2')
#     print(10/0)
#     print('3')
#     try:
#         print('4')
#         print('5')
#     except Exception as e:
#         print(e)
# except Exception as e:
#     print(e)  # division by zero

# Ex=10
# try:
#     print(20+'sonu')
#     try:
#         print(20+'sonu')
#     except Exception as e:
#         print('test hi-: ',e)
#     finally:
#         print('Inner finally block')
# except Exception as e:
#     print('Exception-: ',e)  # Exception-:  unsupported operand type(s) for +: 'int' and 'str'
# finally:
#     print('Outer finally block')

# Ex=11
# try:
#     print('10'+'sonu')
#     try:
#         print(10+'sonu')
#     except Exception as e:
#         print(e)  # unsupported operand type(s) for +: 'int' and 'str'
#     finally:
#         print(10/0)
# except Exception as e:
#     print(e)  # division by zero

# Ex=12
# try:
#     print('10'+'sonu')
#     try:
#         print(10+'sonu')
#     except Exception as e:
#         print(e)  # unsupported operand type(s) for +: 'int' and 'str'
#     finally:
#         print(10/0)
# except FileNotFoundError as f:
#     print(f)
# except Exception as e:
#     print(e)  # division by zero

# Ex=13
# try:
#     print('10'+'sonu')
#     try:
#         print(10+'sonu')
#     except Exception as e:
#         print(e)  # unsupported operand type(s) for +: 'int' and 'str'
#     finally:
#         print('Sudhansu')
#         print(10/2)
#         print('swagatika')
# except FileNotFoundError as f:
#     print(f)
# except Exception as e:
#     print(e)

# Ex=14
# def fun():
#     if (1>1):
#         return True
#     else:
#         return False
#     return 10
#     try:
#         print(1)
#     except Exception as e:
#         print(e)
#     finally:
#         return 99
# print(fun())  # False

# Ex=15
# def fun():
#     try:
#         return 100
#     except:
#         return 200
#     finally:
#         return 300
# print(fun())  # 300

# Ex=16
# def fun():
#     return 10
#     try:
#         return 20
#     except:
#         return 30
#     finally:
#         return 40
# print(fun())  # 10