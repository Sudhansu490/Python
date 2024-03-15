# Exception
# It is a Runtime Error & an unwanted event.
# It disturbs the normal flow of execution.
# If Exception will occur then we can't expect Normal Execution or Smooth Execution.

# Ex=1
# l=[10,20,30,40,50]
# print(l[99])  # IndexError: list index out of range
# for i in range(3):
#     print(i)

# Ex=2
# print('1')
# print('2')
# print('3')
# print(10/'sonu')  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# print('4')
# print('5')

# Ex=3
# i=int(input('Enter i Value:'))
# j=int(input('Enter j Value:'))
# print(i/j)  # ZeroDivisionError: division by zero

# ---------------------------------------------------------------------------------

# Exception Handling
# It is a technique or mechanism to handle Exception.
# If Exception handled successfully then we can expect Smooth Termination.

# Ex=1
# l=[10,20,30,40,50]
# try:
#     print(l[99])
# except Exception as e:
#     print(e)
# for i in range(3):
#     print(i)

# Ex=2
# print('1')
# print('2')
# print('3')
# try:
#     print(10/'sonu')
# except Exception as e:
#     print(e)
# print('4')
# print('5')

# Ex=3
# i=int(input('Enter i Value:'))
# j=int(input('Enter j Value:'))
# try:  # type 1
#     print(i/j)
# except Exception as e:
#     print(e)
# try:  # type 2
#     print(i/j)
# except ZeroDivisionError as z:
#     print(z)
#     print('Hey user! You cannot divide any number with zero.')

# ------------------------------------------------------------------

# i=int(input('Enter i Value:'))
# j=int(input('Enter j Value:'))
# l=[10,20,30,40,50]
# try:
#     print(l[99])  # IndexError: list index out of range
#     print(i/j)
# except ZeroDivisionError as z:
#     print(z)
# Here we only handle the zero division error but we dont handle the IndexError that's why we get the Error.

# i=int(input('Enter i Value:'))
# j=int(input('Enter j Value:'))
# l=[10,20,30,40,50]
# try:
#     print(i/j)
#     print(l[99])  
# except ZeroDivisionError:
#     print('Hey user! You cannot divide any number with zero.') 
# except IndexError:
#     print('Hey user! You cannot access out of range index value.')

# ------------------------------------------------------------------

# Default Exception Handling
# In python if any Exception will raise then PVM(Python Virtual Machine) will create the corresponding exception object.
# Then it will check the corresponding handling code, if handling code is available then no problem or else it will print the Exception information and program will terminate abnormally.

# Ex=1(Here PVM dont find the handling code so the program terminate abnormally.)
# a=10
# b='sony'
# print(a/b)
# print('Thanks')

# Ex=2 
# try:
#     f=open('myfile.txt')
# except FileNotFoundError:
#     print('File does not exist.')
# print('Thank You.')