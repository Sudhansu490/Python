# Try Block-: Inside Try block we will write Critical/Dangerous/Risky code.
# Except Block-: Inside Except block we will write corresponding handling code.

# System Define Exceptions-:
# --------------------------
# 1.NameError
# a=int(input('Enter a value:'))
# b=int(input('Enter b Value:'))
# print(a+c)  # NameError: name 'c' is not defined

# NameError Solution
# a=int(input('Enter a Value:'))
# b=int(input('Enter b Value:'))
# try:
#     print(a+c)
# except NameError as ne:
#     print('Exception Information = ',ne)  # name 'c' is not defined
#     print(type(ne))  # <class 'NameError'>

# --------------------------------------------------------------------
# 2.TypeError
# x=10+'sonu'
# print(x)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# TypeError Solution
# try:
#     x=int(input('Enter Your Roll:')) + input('Enter Your Name:')
# except TypeError as te:
#     print('Exception Information = ',te)

# ------------------------------------
# 3.ValueError
# x=int(input('Enter a Value:'))
# print(x)

# ValueError Solution
# try:
#     x=int(input('Enter a Value:'))
# except ValueError as ve:
#     print('Exception Information =',ve)

# -----------------------------------------
# 4.IndexError
# l=[10,20,30,40,50]
# print(l[8])

# IndexError Solution
# l=[10,20,30,40,50]
# try:
#     print(l[int(input('Enter List Index:'))])
# except IndexError as ie:
#     print('Exception Information =',ie)
#     print(f'hey user, the list range is-:',len(l)-1)

# ----------------------------------------------------
# 5.KeyError
# d={23:'Sonu',24:'Titu',25:'Lina',26:'Rali'}
# print(d[50])

# KeyError Solution
# d={23:'Sonu',24:'Titu',25:'Lina',26:'Rali'}
# try:
#     print(d[int(input('Enter Key Value:'))])
# except KeyError as ke:
#     print('Exception Information(KeyError) =',ke)

# -------------------------------------------------
# 6.FileNotFoundError
# f=open('abc.txt')

# FileNotFoundError Solution
# try:
#     f=open('abc.txt')
# except FileNotFoundError as fnfe:
#     print('Exception Information =',fnfe)

# ---------------------------------------
# 7.ModuleNotFoundError
# import pyqt5

# ModuleNotFoundError Solution
# try:
#     import pyqt5
# except ModuleNotFoundError as mnfe:
#     print('Exception Information =',mnfe)

# -----------------------------------------
# 8.OverflowError
# import math
# print(math.factorial(5623296232123481394))

# OverflowEror Solution
# import math
# try:
#     print(math.factorial(530650356523234531))
# except OverflowError as oe:
#     print('Exception Information =',oe)

# --------------------------------------------
# 9.IndentationError
# It is a type of SyntaxError.
# We can't handle the IndentationError.
# if 10>5:
# print('Hello')

# IndentationError Solution(Impossible)
# try:
#     if 10>5:
#     print('Hello')
# except IndentationError as ite:
#     print('Exception Information =',ite)  # IndentationError

# IndentationError Solution
# try:
#     if 10>5:
#         print('Hello')
# except IndentationError as iee:
#     print('Exception Information =',iee)