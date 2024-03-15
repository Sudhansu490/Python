# Try Except block flow of Execution

# Ex=1
# try:
#     print('1')
#     print(10/0)
#     print('2')
# except ZeroDivisionError as zde:
#     print(zde)
# print('Last Line')
# NOTE-: Try to write very less code inside 'try' block.

# Ex=2
# try:
#     print(10/0)  # after this it directly go to except block 
#     print(20/0)  # this is not executed
# except ZeroDivisionError as ze:
#     print(ze)
# print('Last Line')

# Ex=3
# try:
#     print('1')
#     print(10/0)
# except ZeroDivisionError as z:
#     print(z)
#     print(20/0)  # to handle the above exception another exception raised
# print('Last Line')

# Ex=4
# try:
#     print('1')
#     print(10/0)
# except ZeroDivisionError as z:
#     print(z)
#     try:
#         print(10+'Sonu')
#     except TypeError as t:
#         print(t)
# print('Last Line')

# Ex=5
# try:
#     print(10/0)
# except ArithmeticError as a:
#     print(a)  # ArithmeticError is the father of ZeroDivisionError
# print('Last Line')

# Ex=6(the corresponding try block exception always gets more priority then other except block it doesnot throw any error)
# try:
#     print(10+20)
#     try:
#         print(10/0)
#     except FileNotFoundError as f:
#         print(f)
# except ZeroDivisionError as z:
#     print(z)
# print('Last Line')

# ------------------------------------------------------------------------------------------------------

# Try with multiple Except block, single Except block can handle multiple Exceptions
# Sometimes we can multiple Exceptions from try block, at that time we can go for multiple Except block.

# Ex=1
# try:
#     a=int(input('Enter the value:'))  # 10
#     b=int(input('Enter the value:'))  # sonu
#     result=a/b
#     print(result)
# except ZeroDivisionError as z:
#     print(z)

# Ex=2(try with mmultiple Except block)
# try:
#     a=int(input('Enter the value:'))
#     b=int(input('Enter the value:'))
#     result=a/b 
#     print(result)
# except ValueError as v:
#     print(v)
# except ZeroDivisionError as z:
#     print(z)

# Ex=3
# try:
#     a=int(input('Enter a value:'))  # 100
#     b=int(input('Enter b value:'))  # 20
#     c=a/b
#     print('C is = ',c)
#     x=input('Enter x value:')  # sonu
#     d=a+x
#     print('D is = ',d)
# except ZeroDivisionError as z:
#     print(z)
# except ValueError as v:
#     print(v)
# except TypeError as t:
#     print(t)

# Ex=4
# try:
#     a=int(input('Enter a value:'))
#     b=int(input('Enter b value:'))
#     result=a/b
#     print(result)
# except (ZeroDivisionError,ValueError) as e:
#     print(e)

# Ex=5
# try:
#     a=int(input('Enter a value:'))
#     b=int(input('Enter b value:'))
#     result=a/b
#     print(result)
# except:  # it will handle all type of Exceptions  
#     print('Something goes Wrong!!!')