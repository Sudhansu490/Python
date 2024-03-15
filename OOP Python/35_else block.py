# If there is no exception in try block then else block will be execute.
# Here order is important(try-except-else-finally)

# Ex=1
# try:
#     print(10/0)
# except ZeroDivisionError as z:
#     print(z)
# else:
#     print('I am else block')
# Here else block is not executing because of there is an exception in try block

# Ex=2
# try:
#    print(10/2)
# except ZeroDivisionError as z:
#     print(z)
# else:
#     print('I am else block')
# Here else block is executing because of there is no exception in try block. 

# Ex=3[order is important(try-except-else-finally)]
# def add(a,b):
#     try:
#         result=a+b
#     except TypeError as t:
#         print(t)
#     else:
#         print('Addition reslut is-:',result)
#     finally:
#         print('Clean-up codes')
# add(10,20)
# add(50,'sonu')